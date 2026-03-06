# constantes.py

# --- PALETA DE COLORES ---
# Primary: #102A68, Secondary: #C8102E, Bg: #F4F6F9

# --- 1. FASE DE GRUPOS (FIXTURE COMPLETO) ---
GRUPOS = {
    "GRUPO A": [
        {"id": "A1", "fecha": "11/06 15:00", "sede": "CDMX", "t1": "México", "t2": "Sudáfrica", "bandera1": "🇲🇽", "bandera2": "🇿🇦"},
        {"id": "A2", "fecha": "11/06 22:00", "sede": "Guadalajara", "t1": "Corea del Sur", "t2": "Dinamarca", "bandera1": "🇰🇷", "bandera2": "🇩🇰"},
        {"id": "A3", "fecha": "24/06 21:00", "sede": "CDMX", "t1": "Dinamarca", "t2": "México", "bandera1": "🇩🇰", "bandera2": "🇲🇽"},
        {"id": "A4", "fecha": "24/06 21:00", "sede": "Monterrey", "t1": "Sudáfrica", "t2": "Corea del Sur", "bandera1": "🇿🇦", "bandera2": "🇰🇷"},
    ],
    "GRUPO B": [
        {"id": "B1", "fecha": "12/06 15:00", "sede": "Toronto", "t1": "Canadá", "t2": "Italia", "bandera1": "🇨🇦", "bandera2": "🇮🇹"},
        {"id": "B2", "fecha": "13/06 15:00", "sede": "Bahía SF", "t1": "Catar", "t2": "Suiza", "bandera1": "🇶🇦", "bandera2": "🇨🇭"},
        {"id": "B3", "fecha": "24/06 15:00", "sede": "Vancouver", "t1": "Suiza", "t2": "Canadá", "bandera1": "🇨🇭", "bandera2": "🇨🇦"},
        {"id": "B4", "fecha": "24/06 15:00", "sede": "Seattle", "t1": "Italia", "t2": "Catar", "bandera1": "🇮🇹", "bandera2": "🇶🇦"},
    ],
    "GRUPO C": [
        {"id": "C1", "fecha": "13/06 18:00", "sede": "NY/NJ", "t1": "Brasil", "t2": "Marruecos", "bandera1": "🇧🇷", "bandera2": "🇲🇦"},
        {"id": "C2", "fecha": "13/06 21:00", "sede": "Boston", "t1": "Haití", "t2": "Escocia", "bandera1": "🇭🇹", "bandera2": "🏴󠁧󠁢󠁳󠁣󠁴󠁿"},
        {"id": "C3", "fecha": "24/06 18:00", "sede": "Miami", "t1": "Brasil", "t2": "Escocia", "bandera1": "🇧🇷", "bandera2": "🏴󠁧󠁢󠁳󠁣󠁴󠁿"},
        {"id": "C4", "fecha": "24/06 18:00", "sede": "Atlanta", "t1": "Marruecos", "t2": "Haití", "bandera1": "🇲🇦", "bandera2": "🇭🇹"},
    ],
    "GRUPO D": [
        {"id": "D1", "fecha": "12/06 21:00", "sede": "Los Ángeles", "t1": "EE.UU.", "t2": "Paraguay", "bandera1": "🇺🇸", "bandera2": "🇵🇾"},
        {"id": "D2", "fecha": "13/06 00:00", "sede": "Vancouver", "t1": "Australia", "t2": "Turquía", "bandera1": "🇦🇺", "bandera2": "🇹🇷"},
        {"id": "D3", "fecha": "25/06 22:00", "sede": "Los Ángeles", "t1": "Turquía", "t2": "EE.UU.", "bandera1": "🇹🇷", "bandera2": "🇺🇸"},
        {"id": "D4", "fecha": "25/06 22:00", "sede": "Bahía SF", "t1": "Paraguay", "t2": "Australia", "bandera1": "🇵🇾", "bandera2": "🇦🇺"},
    ],
    "GRUPO E": [
        {"id": "E1", "fecha": "14/06 13:00", "sede": "Houston", "t1": "Alemania", "t2": "Curazao", "bandera1": "🇩🇪", "bandera2": "🇨🇼"},
        {"id": "E2", "fecha": "14/06 19:00", "sede": "Filadelfia", "t1": "C. de Marfil", "t2": "Ecuador", "bandera1": "🇨🇮", "bandera2": "🇪🇨"},
        {"id": "E3", "fecha": "25/06 16:00", "sede": "Filadelfia", "t1": "Curazao", "t2": "C. de Marfil", "bandera1": "🇨🇼", "bandera2": "🇨🇮"},
        {"id": "E4", "fecha": "25/06 16:00", "sede": "NY/NJ", "t1": "Ecuador", "t2": "Alemania", "bandera1": "🇪🇨", "bandera2": "🇩🇪"},
    ],
    "GRUPO F": [
        {"id": "F1", "fecha": "14/06 16:00", "sede": "Dallas", "t1": "Países Bajos", "t2": "Japón", "bandera1": "🇳🇱", "bandera2": "🇯🇵"},
        {"id": "F2", "fecha": "14/06 22:00", "sede": "Monterrey", "t1": "Ucrania", "t2": "Túnez", "bandera1": "🇺🇦", "bandera2": "🇹🇳"},
        {"id": "F3", "fecha": "25/06 19:00", "sede": "Dallas", "t1": "Japón", "t2": "Ucrania", "bandera1": "🇯🇵", "bandera2": "🇺🇦"},
        {"id": "F4", "fecha": "25/06 19:00", "sede": "Kansas City", "t1": "Túnez", "t2": "Países Bajos", "bandera1": "🇹🇳", "bandera2": "🇳🇱"},
    ],
    "GRUPO G": [
        {"id": "G1", "fecha": "15/06 15:00", "sede": "Seattle", "t1": "Bélgica", "t2": "Egipto", "bandera1": "🇧🇪", "bandera2": "🇪🇬"},
        {"id": "G2", "fecha": "15/06 21:00", "sede": "Los Ángeles", "t1": "Irán", "t2": "Nueva Zelanda", "bandera1": "🇮🇷", "bandera2": "🇳🇿"},
        {"id": "G3", "fecha": "21/06 15:00", "sede": "Los Ángeles", "t1": "Bélgica", "t2": "Irán", "bandera1": "🇧🇪", "bandera2": "🇮🇷"},
        {"id": "G4", "fecha": "21/06 21:00", "sede": "Vancouver", "t1": "Nueva Zelanda", "t2": "Egipto", "bandera1": "🇳🇿", "bandera2": "🇪🇬"},
        {"id": "G5", "fecha": "26/06 23:00", "sede": "Seattle", "t1": "Egipto", "t2": "Irán", "bandera1": "🇪🇬", "bandera2": "🇮🇷"},
        {"id": "G6", "fecha": "26/06 23:00", "sede": "Vancouver", "t1": "Nueva Zelanda", "t2": "Bélgica", "bandera1": "🇳🇿", "bandera2": "🇧🇪"},
    ],
    "GRUPO H": [
        {"id": "H1", "fecha": "15/06 12:00", "sede": "Atlanta", "t1": "España", "t2": "Cabo Verde", "bandera1": "🇪🇸", "bandera2": "🇨🇻"},
        {"id": "H2", "fecha": "15/06 18:00", "sede": "Miami", "t1": "Arabia Saudí", "t2": "Uruguay", "bandera1": "🇸🇦", "bandera2": "🇺🇾"},
        {"id": "H3", "fecha": "21/06 12:00", "sede": "Atlanta", "t1": "España", "t2": "Arabia Saudí", "bandera1": "🇪🇸", "bandera2": "🇸🇦"},
        {"id": "H4", "fecha": "21/06 18:00", "sede": "Miami", "t1": "Uruguay", "t2": "Cabo Verde", "bandera1": "🇺🇾", "bandera2": "🇨🇻"},
        {"id": "H5", "fecha": "26/06 20:00", "sede": "Houston", "t1": "Cabo Verde", "t2": "Arabia Saudí", "bandera1": "🇨🇻", "bandera2": "🇸🇦"},
        {"id": "H6", "fecha": "26/06 20:00", "sede": "Guadalajara", "t1": "Uruguay", "t2": "España", "bandera1": "🇺🇾", "bandera2": "🇪🇸"},
    ],
    "GRUPO I": [
        {"id": "I1", "fecha": "16/06 15:00", "sede": "NY/NJ", "t1": "Francia", "t2": "Senegal", "bandera1": "🇫🇷", "bandera2": "🇸🇳"},
        {"id": "I2", "fecha": "16/06 18:00", "sede": "Boston", "t1": "Bolivia", "t2": "Noruega", "bandera1": "🇧🇴", "bandera2": "🇳🇴"},
        {"id": "I3", "fecha": "22/06 17:00", "sede": "Filadelfia", "t1": "Francia", "t2": "Bolivia", "bandera1": "🇫🇷", "bandera2": "🇧🇴"},
        {"id": "I4", "fecha": "22/06 20:00", "sede": "NY/NJ", "t1": "Noruega", "t2": "Senegal", "bandera1": "🇳🇴", "bandera2": "🇸🇳"},
        {"id": "I5", "fecha": "26/06 15:00", "sede": "Boston", "t1": "Noruega", "t2": "Francia", "bandera1": "🇳🇴", "bandera2": "🇫🇷"},
        {"id": "I6", "fecha": "26/06 15:00", "sede": "Toronto", "t1": "Senegal", "t2": "Bolivia", "bandera1": "🇸🇳", "bandera2": "🇧🇴"},
    ],
    "GRUPO J": [
        {"id": "J1", "fecha": "16/06 21:00", "sede": "Kansas City", "t1": "Argentina", "t2": "Argelia", "bandera1": "🇦🇷", "bandera2": "🇩🇿"},
        {"id": "J2", "fecha": "16/06 00:00", "sede": "Bahía SF", "t1": "Austria", "t2": "Jordania", "bandera1": "🇦🇹", "bandera2": "🇯🇴"},
        {"id": "J3", "fecha": "22/06 13:00", "sede": "Dallas", "t1": "Argentina", "t2": "Austria", "bandera1": "🇦🇷", "bandera2": "🇦🇹"},
        {"id": "J4", "fecha": "22/06 23:00", "sede": "Bahía SF", "t1": "Jordania", "t2": "Argelia", "bandera1": "🇯🇴", "bandera2": "🇩🇿"},
        {"id": "J5", "fecha": "27/06 22:00", "sede": "Kansas City", "t1": "Argelia", "t2": "Austria", "bandera1": "🇩🇿", "bandera2": "🇦🇹"},
        {"id": "J6", "fecha": "27/06 22:00", "sede": "Dallas", "t1": "Jordania", "t2": "Argentina", "bandera1": "🇯🇴", "bandera2": "🇦🇷"},
    ],
    "GRUPO K": [
        {"id": "K1", "fecha": "17/06 13:00", "sede": "Houston", "t1": "Portugal", "t2": "Jamaica", "bandera1": "🇵🇹", "bandera2": "🇯🇲"},
        {"id": "K2", "fecha": "17/06 22:00", "sede": "CDMX", "t1": "Uzbekistán", "t2": "Colombia", "bandera1": "🇺🇿", "bandera2": "🇨🇴"},
        {"id": "K3", "fecha": "23/06 13:00", "sede": "Houston", "t1": "Portugal", "t2": "Uzbekistán", "bandera1": "🇵🇹", "bandera2": "🇺🇿"},
        {"id": "K4", "fecha": "23/06 22:00", "sede": "Guadalajara", "t1": "Colombia", "t2": "RD Congo", "bandera1": "🇨🇴", "bandera2": "🇨🇩"},
        {"id": "K5", "fecha": "27/06 19:30", "sede": "Miami", "t1": "Colombia", "t2": "Portugal", "bandera1": "🇨🇴", "bandera2": "🇵🇹"},
        {"id": "K6", "fecha": "27/06 19:30", "sede": "Atlanta", "t1": "RD Congo", "t2": "Uzbekistán", "bandera1": "🇨🇩", "bandera2": "🇺🇿"},
    ],
    "GRUPO L": [
        {"id": "L1", "fecha": "17/06 16:00", "sede": "Dallas", "t1": "Inglaterra", "t2": "Croacia", "bandera1": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "bandera2": "🇭🇷"},
        {"id": "L2", "fecha": "17/06 19:00", "sede": "Toronto", "t1": "Ghana", "t2": "Panamá", "bandera1": "🇬🇭", "bandera2": "🇵🇦"},
        {"id": "L3", "fecha": "23/06 16:00", "sede": "Boston", "t1": "Inglaterra", "t2": "Ghana", "bandera1": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "bandera2": "🇬🇭"},
        {"id": "L4", "fecha": "23/06 19:00", "sede": "Toronto", "t1": "Panamá", "t2": "Croacia", "bandera1": "🇵🇦", "bandera2": "🇭🇷"},
        {"id": "L5", "fecha": "27/06 17:00", "sede": "NY/NJ", "t1": "Panamá", "t2": "Inglaterra", "bandera1": "🇵🇦", "bandera2": "🏴󠁧󠁢󠁥󠁮󠁧󠁿"},
        {"id": "L6", "fecha": "27/06 17:00", "sede": "Filadelfia", "t1": "Croacia", "t2": "Ghana", "bandera1": "🇭🇷", "bandera2": "🇬🇭"},
    ],
}

# --- 2. LISTA PARA ELIMINATORIAS (APP.PY) ---
KNOCKOUT = [
    # Dieciseisavos
    {"id": "P73", "phase": "Dieciseisavos", "fecha": "28/06", "sede": "Los Ángeles", "desc": "2º Grupo A v 2º Grupo B"},
    {"id": "P74", "phase": "Dieciseisavos", "fecha": "29/06", "sede": "Boston", "desc": "1º Grupo E v 3º Grupo A/B/C/D/F"},
    {"id": "P75", "phase": "Dieciseisavos", "fecha": "29/06", "sede": "Monterrey", "desc": "1º Grupo F v 2º Grupo C"},
    {"id": "P76", "phase": "Dieciseisavos", "fecha": "29/06", "sede": "Houston", "desc": "1º Grupo E v 2º Grupo F"},
    {"id": "P77", "phase": "Dieciseisavos", "fecha": "30/06", "sede": "NY/NJ", "desc": "1º Grupo I v 3º Grupo C/D/F/G/H"},
    {"id": "P78", "phase": "Dieciseisavos", "fecha": "30/06", "sede": "Dallas", "desc": "2º Grupo E v 2º Grupo I"},
    {"id": "P79", "phase": "Dieciseisavos", "fecha": "30/06", "sede": "CDMX", "desc": "1º Grupo A v 3º Grupo C/E/F/H/I"},
    {"id": "P80", "phase": "Dieciseisavos", "fecha": "01/07", "sede": "Atlanta", "desc": "1º Grupo L v 3º Grupo E/H/I/J/K"},
    {"id": "P81", "phase": "Dieciseisavos", "fecha": "01/07", "sede": "Bahía SF", "desc": "1º Grupo D v 3º Grupo B/E/F/I/J"},
    {"id": "P82", "phase": "Dieciseisavos", "fecha": "01/07", "sede": "Seattle", "desc": "1º Grupo G v 3º Grupo A/E/H/I/J"},
    {"id": "P83", "phase": "Dieciseisavos", "fecha": "02/07", "sede": "Toronto", "desc": "2º Grupo K v 2º Grupo L"},
    {"id": "P84", "phase": "Dieciseisavos", "fecha": "02/07", "sede": "Los Ángeles", "desc": "1º Grupo H v 2º Grupo J"},
    {"id": "P85", "phase": "Dieciseisavos", "fecha": "02/07", "sede": "Vancouver", "desc": "1º Grupo B v 3º Grupo E/F/G/I/J"},
    {"id": "P86", "phase": "Dieciseisavos", "fecha": "03/07", "sede": "Miami", "desc": "1º Grupo J v 2º Grupo H"},
    {"id": "P87", "phase": "Dieciseisavos", "fecha": "03/07", "sede": "Kansas City", "desc": "1º Grupo K v 3º Grupo D/E/I/J/L"},
    {"id": "P88", "phase": "Dieciseisavos", "fecha": "03/07", "sede": "Dallas", "desc": "2º Grupo D v 2º Grupo G"},

    # Octavos
    {"id": "P89", "phase": "Octavos", "fecha": "04/07", "sede": "Filadelfia", "desc": "Ganador P74 v Ganador P77"},
    {"id": "P90", "phase": "Octavos", "fecha": "04/07", "sede": "Houston", "desc": "Ganador P73 v Ganador P75"},
    {"id": "P91", "phase": "Octavos", "fecha": "05/07", "sede": "NY/NJ", "desc": "Ganador P76 v Ganador P78"},
    {"id": "P92", "phase": "Octavos", "fecha": "05/07", "sede": "CDMX", "desc": "Ganador P79 v Ganador P80"},
    {"id": "P93", "phase": "Octavos", "fecha": "06/07", "sede": "Dallas", "desc": "Ganador P83 v Ganador P84"},
    {"id": "P94", "phase": "Octavos", "fecha": "06/07", "sede": "Seattle", "desc": "Ganador P81 v Ganador P82"},
    {"id": "P95", "phase": "Octavos", "fecha": "07/07", "sede": "Atlanta", "desc": "Ganador P86 v Ganador P88"},
    {"id": "P96", "phase": "Octavos", "fecha": "07/07", "sede": "Vancouver", "desc": "Ganador P85 v Ganador P87"},

    # Cuartos
    {"id": "P97", "phase": "Cuartos", "fecha": "09/07", "sede": "Boston", "desc": "Ganador P89 v Ganador P90"},
    {"id": "P98", "phase": "Cuartos", "fecha": "10/07", "sede": "Los Ángeles", "desc": "Ganador P93 v Ganador P94"},
    {"id": "P99", "phase": "Cuartos", "fecha": "11/07", "sede": "Miami", "desc": "Ganador P91 v Ganador P92"},
    {"id": "P100", "phase": "Cuartos", "fecha": "11/07", "sede": "Kansas City", "desc": "Ganador P95 v Ganador P96"},

    # Semifinales
    {"id": "SEMI1", "phase": "Semifinales", "fecha": "14/07", "sede": "Dallas", "desc": "Ganador P97 v Ganador P99"},
    {"id": "SEMI2", "phase": "Semifinales", "fecha": "15/07", "sede": "Atlanta", "desc": "Ganador P98 v Ganador P100"},

    # Tercer Puesto y Final
    {"id": "P103", "phase": "Tercer Puesto", "fecha": "18/07", "sede": "Miami", "desc": "Perdedor S1 v Perdedor S2"},
    {"id": "P104", "phase": "Final", "fecha": "19/07", "sede": "NY/NJ", "desc": "Ganador S1 v Ganador S2"}
]

# --- 3. ESTRUCTURA LÓGICA DE PROPAGACIÓN (BRACKET) ---
ESTRUCTURA_MUNDIAL_2026 = {
    # DIECISEISAVOS (Equipos vienen de Grupos -> Destino Octavos)
    'P73': {'origen': ['2º Grupo A', '2º Grupo B'], 'destino': 'P90', 'pos_destino': 0},
    'P74': {'origen': ['1º Grupo E', '3º Grupo A/B/C/D/F'], 'destino': 'P89', 'pos_destino': 0},
    'P75': {'origen': ['1º Grupo F', '2º Grupo C'], 'destino': 'P90', 'pos_destino': 1},
    'P76': {'origen': ['1º Grupo E', '2º Grupo F'], 'destino': 'P91', 'pos_destino': 0},
    'P77': {'origen': ['1º Grupo I', '3º Grupo C/D/F/G/H'], 'destino': 'P89', 'pos_destino': 1},
    'P78': {'origen': ['2º Grupo E', '2º Grupo I'], 'destino': 'P91', 'pos_destino': 1},
    'P79': {'origen': ['1º Grupo A', '3º Grupo C/E/F/H/I'], 'destino': 'P92', 'pos_destino': 0},
    'P80': {'origen': ['1º Grupo L', '3º Grupo E/H/I/J/K'], 'destino': 'P92', 'pos_destino': 1},
    'P81': {'origen': ['1º Grupo D', '3º Grupo B/E/F/I/J'], 'destino': 'P94', 'pos_destino': 0},
    'P82': {'origen': ['1º Grupo G', '3º Grupo A/E/H/I/J'], 'destino': 'P94', 'pos_destino': 1},
    'P83': {'origen': ['2º Grupo K', '2º Grupo L'], 'destino': 'P93', 'pos_destino': 0},
    'P84': {'origen': ['1º Grupo H', '2º Grupo J'], 'destino': 'P93', 'pos_destino': 1},
    'P85': {'origen': ['1º Grupo B', '3º Grupo E/F/G/I/J'], 'destino': 'P96', 'pos_destino': 0},
    'P86': {'origen': ['1º Grupo J', '2º Grupo H'], 'destino': 'P95', 'pos_destino': 0},
    'P87': {'origen': ['1º Grupo K', '3º Grupo D/E/I/J/L'], 'destino': 'P96', 'pos_destino': 1},
    'P88': {'origen': ['2º Grupo D', '2º Grupo G'], 'destino': 'P95', 'pos_destino': 1},

    # OCTAVOS (Destino Cuartos)
    'P89': {'origen': ['Ganador P74', 'Ganador P77'], 'destino': 'P97', 'pos_destino': 0},
    'P90': {'origen': ['Ganador P73', 'Ganador P75'], 'destino': 'P97', 'pos_destino': 1},
    'P91': {'origen': ['Ganador P76', 'Ganador P78'], 'destino': 'P99', 'pos_destino': 0},
    'P92': {'origen': ['Ganador P79', 'Ganador P80'], 'destino': 'P99', 'pos_destino': 1},
    'P93': {'origen': ['Ganador P83', 'Ganador P84'], 'destino': 'P98', 'pos_destino': 0},
    'P94': {'origen': ['Ganador P81', 'Ganador P82'], 'destino': 'P98', 'pos_destino': 1},
    'P95': {'origen': ['Ganador P86', 'Ganador P88'], 'destino': 'P100', 'pos_destino': 0},
    'P96': {'origen': ['Ganador P85', 'Ganador P87'], 'destino': 'P100', 'pos_destino': 1},

    # CUARTOS (Destino Semis)
    'P97': {'origen': ['Ganador P89', 'Ganador P90'], 'destino': 'SEMI1', 'pos_destino': 0},
    'P98': {'origen': ['Ganador P93', 'Ganador P94'], 'destino': 'SEMI2', 'pos_destino': 0},
    'P99': {'origen': ['Ganador P91', 'Ganador P92'], 'destino': 'SEMI1', 'pos_destino': 1},
    'P100': {'origen': ['Ganador P95', 'Ganador P96'], 'destino': 'SEMI2', 'pos_destino': 1},

    # SEMIS (Destino Final)
    'SEMI1': {'origen': ['Ganador P97', 'Ganador P99'], 'destino': 'P104', 'pos_destino': 0},
    'SEMI2': {'origen': ['Ganador P98', 'Ganador P100'], 'destino': 'P104', 'pos_destino': 1},

    # TERCER PUESTO Y FINAL
    'P103': {'origen': ['Perdedor S1', 'Perdedor S2'], 'destino': None, 'pos_destino': None},
    'P104': {'origen': ['Ganador S1', 'Ganador S2'], 'destino': None, 'pos_destino': None}
}
# --- 4. LISTA DE PAÍSES PARA ASIGNACIÓN ---
COUNTRIES = [
    {"name": "Argentina", "flag": "🇦🇷"}, {"name": "Brasil", "flag": "🇧🇷"},
    {"name": "Uruguay", "flag": "🇺🇾"}, {"name": "Colombia", "flag": "🇨🇴"},
    {"name": "Ecuador", "flag": "🇪🇨"}, {"name": "Perú", "flag": "🇵🇪"},
    {"name": "Chile", "flag": "🇨🇱"}, {"name": "Paraguay", "flag": "🇵🇾"},
    {"name": "Bolivia", "flag": "🇧🇴"}, {"name": "Venezuela", "flag": "🇻🇪"},
    {"name": "México", "flag": "🇲🇽"}, {"name": "EE.UU.", "flag": "🇺🇸"},
    {"name": "Canadá", "flag": "🇨🇦"}, {"name": "Costa Rica", "flag": "🇨🇷"},
    {"name": "Panamá", "flag": "🇵🇦"}, {"name": "Jamaica", "flag": "🇯🇲"},
    {"name": "España", "flag": "🇪��"}, {"name": "Francia", "flag": "🇫🇷"},
    {"name": "Alemania", "flag": "🇩🇪"}, {"name": "Italia", "flag": "🇮🇹"},
    {"name": "Inglaterra", "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿"}, {"name": "Portugal", "flag": "🇵🇹"},
    {"name": "Países Bajos", "flag": "🇳🇱"}, {"name": "Bélgica", "flag": "🇧🇪"},
    {"name": "Croacia", "flag": "🇭🇷"}, {"name": "Suiza", "flag": "🇨🇭"},
    {"name": "Dinamarca", "flag": "🇩🇰"}, {"name": "Serbia", "flag": "🇷🇸"},
    {"name": "Polonia", "flag": "🇵🇱"}, {"name": "Ucrania", "flag": "🇺🇦"},
    {"name": "Marruecos", "flag": "🇲🇦"}, {"name": "Senegal", "flag": "🇸🇳"},
    {"name": "Túnez", "flag": "🇹🇳"}, {"name": "Ghana", "flag": "🇬🇭"},
    {"name": "Camerún", "flag": "🇨🇲"}, {"name": "Nigeria", "flag": "🇳🇬"},
    {"name": "Egipto", "flag": "🇪🇬"}, {"name": "Argelia", "flag": "🇩🇿"},
    {"name": "Costa de Marfil", "flag": "🇨🇮"}, {"name": "Sudáfrica", "flag": "🇿🇦"},
    {"name": "Japón", "flag": "🇯🇵"}, {"name": "Corea del Sur", "flag": "��🇷"},
    {"name": "Australia", "flag": "🇦🇺"}, {"name": "Irán", "flag": "🇮🇷"},
    {"name": "Arabia Saudí", "flag": "🇸🇦"}, {"name": "Catar", "flag": "🇶🇦"},
    {"name": "Nueva Zelanda", "flag": "🇳🇿"}, {"name": "Uzbekistán", "flag": "🇺🇿"},
]
