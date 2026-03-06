from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database.database import get_db
from core.constantes import GRUPOS, KNOCKOUT
import datetime

from routers.auth import get_current_user
from database.models import Prediccion, Usuario, ConfigGlobal
import json
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_sidebar_data(username: str, db: Session):
    user = db.query(Usuario).filter(Usuario.username == username).first()
    if not user:
        return {"puntos": 0, "posicion": "-"}
    puntos = user.puntos_totales or 0
    # Posición es cuántos usuarios tienen estrictamente más puntos + 1
    higher = db.query(Usuario).filter(Usuario.puntos_totales > puntos).count()
    return {"puntos": puntos, "posicion": higher + 1}

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    """Renderiza la vista principal del usuario con los grupos y partidos."""
    
    # Verificación de Autenticación
    username = get_current_user(request)
    if not username:
        return RedirectResponse(url="/login", status_code=303)
        
    # --- LOGICA DEL BANNER CRAWLER ---
    hoy_dt = datetime.datetime.now()
    if hoy_dt.year != 2026 or hoy_dt.month != 6:
        hoy_str = "11/06"
    else:
        hoy_str = hoy_dt.strftime("%d/%m")

    partidos_ticker = []
    
    for g, lista in GRUPOS.items():
        for p in lista:
            if p['fecha'].startswith(hoy_str):
                p_copy = dict(p)
                p_copy['cat_label'] = g
                partidos_ticker.append(p_copy)
    
    for p in KNOCKOUT:
        if p['fecha'].startswith(hoy_str):
            p_copy = dict(p)
            p_copy['cat_label'] = p.get('phase', 'ELIMINATORIA').upper()
            partidos_ticker.append(p_copy)

    def sort_key(partido):
        f = partido['fecha']
        parts = f.split(" ")
        dia_mes = parts[0].split("/")
        orden_dia = int(dia_mes[1]) * 100 + int(dia_mes[0])
        orden_hora = parts[1] if len(parts) > 1 else "00:00"
        return (orden_dia, orden_hora)

    partidos_ticker.sort(key=sort_key)
    
    crawler_items = []
    for p in partidos_ticker:
        t1 = p.get('t1') or "TBD"
        t2 = p.get('t2') or "TBD"
        desc_match = p['desc'] if (t1 == "TBD" and "desc" in p) else f"{t1} vs {t2}"
        cat = p.get('cat_label', '')
        txt = f'<span class="crawler-alert">ALERTA {cat}</span> {desc_match} Juega (HOY)'
        crawler_items.append(txt)

    separador = ' <span class="crawler-separator"> - </span> '
    crawling_text = separador.join(crawler_items) if crawler_items else ""
    if crawling_text:
        crawling_text = crawling_text + separador + crawling_text

    # Extraer las predicciones previas del usuario desde la base de datos
    user_preds = db.query(Prediccion).filter(Prediccion.username == username).first()
    datos_actuales = json.loads(user_preds.datos) if user_preds and user_preds.datos else {}

    # Cargar estado de fases y partidos cerrados desde la BD
    from database.models import ConfigGlobal
    conf_fases = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "fases_estado").first()
    if not conf_fases:
        estados_fases = {"Grupos": True, "Dieciseisavos": False, "Octavos": False, "Cuartos": False, "Semis": False, "Finales": False}
        nueva_conf = ConfigGlobal(clave="fases_estado", valor=json.dumps(estados_fases))
        db.add(nueva_conf)
        db.commit()
    else:
        estados_fases = json.loads(conf_fases.valor)

    conf_cerrados = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "partidos_cerrados").first()
    partidos_cerrados = json.loads(conf_cerrados.valor) if conf_cerrados else []

    # Agrupar partidos KNOCKOUT por fase
    # Extraer asignaciones de equipos para knockout
    conf_asig = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "knockout_asignaciones").first()
    knockout_asignaciones = json.loads(conf_asig.valor) if conf_asig else {}

    # Agrupar partidos KNOCKOUT por fase e inyectar equipos dinámicos
    knockout_por_fase = {}
    for p in KNOCKOUT:
        m_id = p['id']
        asig = knockout_asignaciones.get(m_id)
        p_copy = dict(p)
        if asig:
            p_copy['t1'] = asig['t1']
            p_copy['bandera1'] = asig['bandera1']
            p_copy['t2'] = asig['t2']
            p_copy['bandera2'] = asig['bandera2']
        else:
            p_copy['t1'] = "TBD"
            p_copy['bandera1'] = "🏴"
            p_copy['t2'] = "TBD"
            p_copy['bandera2'] = "🏴"
            
        fase = p_copy.get('phase', 'Eliminatorias')
        if fase not in knockout_por_fase:
            knockout_por_fase[fase] = []
        knockout_por_fase[fase].append(p_copy)

    # Agrupar GRUPOS por fecha
    partidos_por_fecha = {}
    for g_name, lista in GRUPOS.items():
        for p in lista:
            dia = p['fecha'].split(" ")[0]
            if dia not in partidos_por_fecha:
                partidos_por_fecha[dia] = []
            p_copy = dict(p)
            p_copy['grupo'] = g_name
            partidos_por_fecha[dia].append(p_copy)
            
    def sort_fecha(dia_str):
        parts = dia_str.split("/")
        if len(parts) == 2:
            return int(parts[1]) * 100 + int(parts[0])
        return 9999
        
    fechas_ordenadas = sorted(partidos_por_fecha.keys(), key=sort_fecha)
    partidos_agrupados_fecha = {}
    for f in fechas_ordenadas:
        partidos_agrupados_fecha[f] = sorted(partidos_por_fecha[f], key=lambda x: x['fecha'].split(" ")[1] if " " in x['fecha'] else "00:00")

    # Extraer los resultados ya cargados por el admin
    from database.models import DatosOficiales
    from core.scoring import ScoringEngine

    resultados_raw = db.query(DatosOficiales).all()
    resultados_dict = {}
    for r in resultados_raw:
        try:
            resultados_dict[r.match_id] = json.loads(r.datos)
        except:
            pass

    engine = ScoringEngine()
    puntos_por_partido = {}

    for f_name, lista_partidos in partidos_agrupados_fecha.items():
        for p in lista_partidos:
            m_id = p['id']
            off_data = resultados_dict.get(m_id)
            if m_id in partidos_cerrados and off_data and off_data.get("g1") is not None:
                pts = engine._calcular_partido(m_id, datos_actuales, off_data)
                
                real_winner_str = engine._get_winner_str(off_data.get("g1"), off_data.get("g2"))
                is_tie = (real_winner_str == "draw")
                
                base_max = engine.rules.get("exact_score", 6)
                if is_tie and off_data.get("winner"):
                    base_max += engine.rules.get("penalty_bonus", 1)
                    
                phase = engine.match_phases.get(m_id, 'group')
                mult = engine.multipliers.get(phase, 1.0)
                max_possible = int(base_max * mult)
                
                puntos_por_partido[m_id] = {
                    "pts": pts,
                    "is_max": pts == max_possible
                }

    return templates.TemplateResponse("index.html", {
        "request": request,
        "grupos": GRUPOS,
        "partidos_agrupados_fecha": partidos_agrupados_fecha,
        "knockout_por_fase": knockout_por_fase,
        "estados_fases": estados_fases,
        "partidos_cerrados": partidos_cerrados,
        "crawling_text": crawling_text,
        "username": username,
        "datos": datos_actuales,
        "resultados_dict": resultados_dict,
        "puntos_por_partido": puntos_por_partido,
        "sidebar_data": get_sidebar_data(username, db)
    })

@router.post("/predict/{match_id}", response_class=HTMLResponse)
async def predict_match(
    request: Request,
    match_id: str,
    g1: str = Form(None),
    g2: str = Form(None),
    penales: str = Form(None),
    db: Session = Depends(get_db)
):
    """Guarda la predicción parcial del usuario vía HTMX en SQLite."""
    username = get_current_user(request)
    if not username:
        return f'<span style="color: red; font-size: 0.85rem;">⚠️ No autenticado</span>'

    # Verificar si el partido está cerrado administrativamente
    from database.models import ConfigGlobal
    conf_cerrados = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "partidos_cerrados").first()
    partidos_cerrados = json.loads(conf_cerrados.valor) if conf_cerrados else []
    
    if match_id in partidos_cerrados:
        return f'<span style="color: #dc3545; font-size: 0.85rem; font-weight: bold;">🔒 Evento Finalizado</span>'

    # Validación simple: si ambos tienen valor, procesamos el guardado en la DB
    if g1 is not None and g1.strip() != "" and g2 is not None and g2.strip() != "":
        # Buscar usuario en DB
        pred = db.query(Prediccion).filter(Prediccion.username == username).first()
        if not pred:
            pred = Prediccion(username=username, datos="{}")
            db.add(pred)
            db.commit()
            
        # Parsear JSON existente
        datos = json.loads(pred.datos) if pred.datos else {}
        datos[f"{match_id}_g1"] = int(g1)
        datos[f"{match_id}_g2"] = int(g2)
        if penales:
            datos[f"{match_id}_penales"] = penales
        else:
            datos.pop(f"{match_id}_penales", None)
        
        # Volver a guardar JSON
        pred.datos = json.dumps(datos)
        db.commit()
        
        msg = f'<span style="color: #28a745; font-size: 0.85rem; font-weight: bold;">✅ Guardado {g1}-{g2}</span>'
        if int(g1) == int(g2) and penales:
            msg += f'<br><span style="color: #102a68; font-size: 0.8rem;">(Penales: {penales})</span>'
        return msg
    
    return f'<span style="color: #6c757d; font-size: 0.85rem;">⏳ Pendiente</span>'

@router.get("/fixture", response_class=HTMLResponse)
async def ver_fixture(request: Request, db: Session = Depends(get_db)):
    """Renderiza el fixture de grupos mostrando los resultados oficiales y puntajes."""
    username = get_current_user(request)
    if not username:
        return RedirectResponse(url="/login", status_code=303)
        
    try:
        from database.models import DatosOficiales
        from core.scoring import ScoringEngine
        
        # Cargar predicciones
        pred = db.query(Prediccion).filter(Prediccion.username == username).first()
        datos_prediccion = json.loads(pred.datos) if pred and pred.datos else {}
                
        # Cargar resultados
        resultados_raw = db.query(DatosOficiales).all()
        resultados_dict = {}
        for r in resultados_raw:
            try:
                resultados_dict[r.match_id] = json.loads(r.datos)
            except:
                pass

        engine = ScoringEngine()
        
        fixture_grupos = {}
        for grupo_name, partidos in GRUPOS.items():
            fixture_grupos[grupo_name] = []
            for p in partidos:
                m_id = p['id']
                pts = "N/A"
                max_pts = False
                off_data = resultados_dict.get(m_id)
                if off_data and off_data.get("g1") is not None:
                    pts = engine._calcular_partido(m_id, datos_prediccion, off_data)
                    
                    real_winner_str = engine._get_winner_str(off_data.get("g1"), off_data.get("g2"))
                    is_tie = (real_winner_str == "draw")
                    
                    base_max = engine.rules.get("exact_score", 6)
                    if is_tie and off_data.get("winner"):
                        base_max += engine.rules.get("penalty_bonus", 1)
                        
                    phase = engine.match_phases.get(m_id, 'group')
                    mult = engine.multipliers.get(phase, 1.0)
                    max_possible = int(base_max * mult)
                    
                    if pts == max_possible:
                        max_pts = True
                
                p_dict = dict(p)
                p_dict['off_g1'] = off_data.get("g1") if off_data else ""
                p_dict['off_g2'] = off_data.get("g2") if off_data else ""
                p_dict['off_penales'] = off_data.get("winner") if off_data and off_data.get("winner") else ""
                p_dict['user_pts'] = pts
                p_dict['is_max_pts'] = max_pts
                
                fixture_grupos[grupo_name].append(p_dict)
                
        # Extraer asignaciones de equipos para knockout
        conf_asig = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "knockout_asignaciones").first()
        knockout_asignaciones = json.loads(conf_asig.valor) if conf_asig else {}

        # Calcular y pasar también los partidos KNOCKOUT para la llave
        fixture_knockout = []
        for p in KNOCKOUT:
            m_id = p['id']
            asig = knockout_asignaciones.get(m_id)
            p_copy = dict(p)
            
            # Si el admin ya asignó equipos reales, los usamos
            if asig:
                p_copy['t1'] = asig['t1']
                p_copy['bandera1'] = asig['bandera1']
                p_copy['t2'] = asig['t2']
                p_copy['bandera2'] = asig['bandera2']
            # De lo contrario, NO setteamos t1/t2 aquí para que el template use el 'desc' split
            # o mostramos "TBD" si no hay descripción.

            pts = "N/A"
            max_pts = False
            off_data = resultados_dict.get(m_id)
            if off_data and off_data.get("g1") is not None:
                pts = engine._calcular_partido(m_id, datos_prediccion, off_data)
                
                real_winner_str = engine._get_winner_str(off_data.get("g1"), off_data.get("g2"))
                is_tie = (real_winner_str == "draw")
                
                base_max = engine.rules.get("exact_score", 6)
                if is_tie and off_data.get("winner"):
                    base_max += engine.rules.get("penalty_bonus", 1)
                    
                phase = engine.match_phases.get(m_id, 'round_of_32')
                mult = engine.multipliers.get(phase, 1.0)
                max_possible = int(base_max * mult)
                
                if pts == max_possible:
                    max_pts = True
                    
            p_copy['off_g1'] = off_data.get("g1") if off_data else ""
            p_copy['off_g2'] = off_data.get("g2") if off_data else ""
            p_copy['off_penales'] = off_data.get("winner") if off_data and off_data.get("winner") else ""
            p_copy['user_pts'] = pts
            p_copy['is_max_pts'] = max_pts
            
            fixture_knockout.append(p_copy)
                
        return templates.TemplateResponse("fixture.html", {
            "request": request,
            "username": username,
            "fixture_grupos": fixture_grupos,
            "fixture_knockout": fixture_knockout,
            "sidebar_data": get_sidebar_data(username, db)
        })
    except Exception as e:
        import traceback
        print(f"DEBUG Error en ver_fixture: {str(e)}")
        print(traceback.format_exc())
        return HTMLResponse(content=f"Error en servidor: {str(e)}", status_code=500)

@router.get("/ranking", response_class=HTMLResponse)
async def ver_ranking(request: Request, db: Session = Depends(get_db)):
    """Renderiza la tabla de posiciones global."""
    username = get_current_user(request)
    if not username:
        return RedirectResponse(url="/login", status_code=303)
        
    # Extraer todos los usuarios ordenados por puntos descendente (excluyendo admins si se desea, aquí los metemos todos)
    from database.models import Usuario, Premio
    usuarios_ordenados = db.query(Usuario).order_by(Usuario.puntos_totales.desc()).all()
    
    premios = db.query(Premio).order_by(Premio.orden.asc()).all()
    
    return templates.TemplateResponse("ranking.html", {
        "request": request,
        "username": username,
        "usuarios": usuarios_ordenados,
        "sidebar_data": get_sidebar_data(username, db),
        "premios": premios
    })

@router.get("/reglas", response_class=HTMLResponse)
async def ver_reglas(request: Request, db: Session = Depends(get_db)):
    """Renderiza la página estática de reglamento y premios."""
    username = get_current_user(request)
    if not username:
        return RedirectResponse(url="/login", status_code=303)
        
    return templates.TemplateResponse("reglas.html", {
        "request": request,
        "username": username,
        "sidebar_data": get_sidebar_data(username, db)
    })

@router.get("/perfil", response_class=HTMLResponse)
async def ver_perfil(request: Request, db: Session = Depends(get_db)):
    """Renderiza el perfil del usuario activo con su desglose de puntos por partido."""
    username = get_current_user(request)
    if not username:
        return RedirectResponse(url="/login", status_code=303)
        
    from database.models import Usuario, DatosOficiales, Premio
    from core.scoring import ScoringEngine
    
    usuario = db.query(Usuario).filter(Usuario.username == username).first()
    
    premios = db.query(Premio).order_by(Premio.orden.asc()).all()
    
    # Construir historial
    historial = []
    pred = db.query(Prediccion).filter(Prediccion.username == username).first()
    if pred and pred.datos:
        try:
            datos_prediccion = json.loads(pred.datos)
        except:
            datos_prediccion = {}
            
        # Cargar resultados oficiales
        from database.models import DatosOficiales
        resultados_raw = db.query(DatosOficiales).all()

        engine = ScoringEngine()
        
        # Mapear nombres de partidos (incluyendo asignaciones dinámicas)
        conf_asig = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "knockout_asignaciones").first()
        knockout_asignaciones = json.loads(conf_asig.valor) if conf_asig else {}

        nombres_partidos = {}
        
        # Grupos
        for grupo_name, partidos in GRUPOS.items():
            for p in partidos:
                nombres_partidos[p['id']] = {"desc": f"{p['t1']} vs {p['t2']}", "fase": "GRUPOS"}
        
        # Knockout
        for p in KNOCKOUT:
            asig = knockout_asignaciones.get(p['id'])
            if asig:
                desc = f"{asig['t1']} vs {asig['t2']}"
            else:
                desc = f"TBD ({p.get('desc', p['id'])})"
            nombres_partidos[p['id']] = {"desc": desc, "fase": p.get('phase', 'ELIMINATORIAS').upper()}

        for r in resultados_raw:
            try:
                off_data = json.loads(r.datos)
                pts = engine._calcular_partido(r.match_id, datos_prediccion, off_data)
                
                info_p = nombres_partidos.get(r.match_id, {"desc": r.match_id, "fase": ""})
                
                historial.append({
                    "partido": info_p["desc"],
                    "fase": info_p["fase"],
                    "off_g1": off_data.get("g1", "-"),
                    "off_g2": off_data.get("g2", "-"),
                    "pred_g1": datos_prediccion.get(f"{r.match_id}_g1"),
                    "pred_g2": datos_prediccion.get(f"{r.match_id}_g2"),
                    "puntos": pts
                })
            except:
                continue

    return templates.TemplateResponse("perfil.html", {
        "request": request,
        "username": username,
        "usuario": usuario,
        "historial": historial,
        "sidebar_data": get_sidebar_data(username, db),
        "premios": premios
    })
