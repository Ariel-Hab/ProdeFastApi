import json
import random
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import DatosOficiales, Prediccion, Usuario, ConfigGlobal
from core.constantes import KNOCKOUT, ESTRUCTURA_MUNDIAL_2026, COUNTRIES
from core.scoring import ScoringEngine

def get_flag(team_name):
    for c in COUNTRIES:
        if c['name'] == team_name:
            return c['flag']
    return "🏳️"

def simulate_phase(db, phase_name, pepe_hit_rate=0.10, force_winner="Argentina"):
    print(f"--- Simulando Fase: {phase_name} ---")
    
    matches_in_phase = [m for m in KNOCKOUT if m['phase'] == phase_name]
    match_ids = [m['id'] for m in matches_in_phase]
    
    conf_asig = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "knockout_asignaciones").first()
    if not conf_asig: return
    asignaciones = json.loads(conf_asig.valor)
    
    for m_id in match_ids:
        if m_id not in asignaciones:
            continue
            
        t1 = asignaciones[m_id].get('t1', 'TBD')
        t2 = asignaciones[m_id].get('t2', 'TBD')
        
        if t1 == 'TBD' or t2 == 'TBD':
            continue
        
        # Forzar victoria de Argentina (o del force_winner)
        if t1 == force_winner or t2 == force_winner:
            if t1 == force_winner:
                g1 = random.randint(1, 4)
                g2 = random.randint(0, g1 - 1)
            else:
                g2 = random.randint(1, 4)
                g1 = random.randint(0, g2 - 1)
            winner = None
        else:
            g1, g2 = random.randint(0, 3), random.randint(0, 3)
            winner = None
            if g1 == g2:
                winner = t1 if random.random() < 0.5 else t2
        
        oficial = db.query(DatosOficiales).filter(DatosOficiales.match_id == m_id).first()
        oficial_data = {"g1": g1, "g2": g2, "winner": winner}
        if oficial:
            oficial.datos = json.dumps(oficial_data)
        else:
            db.add(DatosOficiales(match_id=m_id, datos=json.dumps(oficial_data)))
            
    # Cerrar partidos
    conf_cerrados = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "partidos_cerrados").first()
    cerrados = json.loads(conf_cerrados.valor) if conf_cerrados else []
    for m_id in match_ids:
        if m_id not in cerrados:
            cerrados.append(m_id)
    if not conf_cerrados:
        db.add(ConfigGlobal(clave="partidos_cerrados", valor=json.dumps(cerrados)))
    else:
        conf_cerrados.valor = json.dumps(cerrados)
        
    db.commit()

    # Generar Predicciones para Pepe
    pepe_pred_obj = db.query(Prediccion).filter(Prediccion.username == "pepe").first()
    pepe_preds = json.loads(pepe_pred_obj.datos) if pepe_pred_obj and pepe_pred_obj.datos else {}
    
    resultados_oficiales = {r.match_id: json.loads(r.datos) for r in db.query(DatosOficiales).all()}
    
    for m_id in match_ids:
        if m_id not in resultados_oficiales or m_id not in asignaciones: continue
        off = resultados_oficiales[m_id]
        o_g1, o_g2 = off['g1'], off['g2']
        o_winner = off.get('winner')
        t1 = asignaciones[m_id].get('t1', 'TBD')
        t2 = asignaciones[m_id].get('t2', 'TBD')
        
        if t1 == 'TBD' or t2 == 'TBD': continue
        
        if random.random() < pepe_hit_rate:
            p_g1, p_g2 = o_g1, o_g2
            if o_g1 == o_g2:
                pepe_preds[f"{m_id}_penales"] = o_winner
        else:
            p_g1, p_g2 = random.randint(0, 4), random.randint(0, 4)
            while p_g1 == o_g1 and p_g2 == o_g2:
                p_g1, p_g2 = random.randint(0, 4), random.randint(0, 4)
            if p_g1 == p_g2:
                pepe_preds[f"{m_id}_penales"] = t1 if random.random() < 0.5 else t2
                
        pepe_preds[f"{m_id}_g1"] = p_g1
        pepe_preds[f"{m_id}_g2"] = p_g2
        
    pepe_pred_obj.datos = json.dumps(pepe_preds)
    db.commit()

    # Propagar Ganadores
    for m_id in match_ids:
        if m_id not in resultados_oficiales or m_id not in asignaciones: continue
        off = resultados_oficiales[m_id]
        o_g1, o_g2 = off['g1'], off['g2']
        o_winner = off.get('winner')
        
        t1 = asignaciones[m_id].get('t1', 'TBD')
        t2 = asignaciones[m_id].get('t2', 'TBD')
        if t1 == 'TBD' or t2 == 'TBD': continue
        
        if o_g1 > o_g2:
            advancing_team = t1
            losing_team = t2
        elif o_g2 > o_g1:
            advancing_team = t2
            losing_team = t1
        else:
            advancing_team = o_winner
            losing_team = t1 if o_winner == t2 else t2
            
        estructura = ESTRUCTURA_MUNDIAL_2026.get(m_id)
        if estructura and estructura['destino']:
            dest_id = estructura['destino']
            pos = estructura['pos_destino'] 
            
            if dest_id not in asignaciones:
                asignaciones[dest_id] = {}
                
            if pos == 0:
                asignaciones[dest_id]['t1'] = advancing_team
                asignaciones[dest_id]['bandera1'] = get_flag(advancing_team)
            else:
                asignaciones[dest_id]['t2'] = advancing_team
                asignaciones[dest_id]['bandera2'] = get_flag(advancing_team)
                
        # Lógica especial para Tercer Puesto (Perdedores de Semis)
        if phase_name == "Semifinales":
            dest_tercer_puesto = "P103"
            if dest_tercer_puesto not in asignaciones:
                asignaciones[dest_tercer_puesto] = {}
            if m_id == "SEMI1":
                asignaciones[dest_tercer_puesto]['t1'] = losing_team
                asignaciones[dest_tercer_puesto]['bandera1'] = get_flag(losing_team)
            elif m_id == "SEMI2":
                asignaciones[dest_tercer_puesto]['t2'] = losing_team
                asignaciones[dest_tercer_puesto]['bandera2'] = get_flag(losing_team)

    conf_asig.valor = json.dumps(asignaciones)
    db.commit()

def main():
    db = SessionLocal()
    try:
        # Check if Argentina is actually mapped
        conf_asig = db.query(ConfigGlobal).filter(ConfigGlobal.clave == "knockout_asignaciones").first()
        if conf_asig:
           asig_str = conf_asig.valor
           if "Argentina" not in asig_str:
               print("Atención: Argentina no está en las llaves, buscaré al equipo que esté en Cuartos para forzarlo...")
               
        phases = ["Cuartos", "Semifinales", "Tercer Puesto", "Final"]
        for p in phases:
            simulate_phase(db, p, 0.10, "Argentina")
            
        print("Recalculando puntajes finales...")
        engine = ScoringEngine()
        engine.recalcular_todo(db)
        
        pepe_final = db.query(Usuario).filter(Usuario.username == "pepe").first()
        print(f"Puntaje total final de Pepe: {pepe_final.puntos_totales}")
        print("✅ Mundial completado. ¡Argentina campeón (si estaba en llaves)!")
    finally:
        db.close()

if __name__ == "__main__":
    main()
