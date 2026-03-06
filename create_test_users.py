import sqlite3

def create_users():
    conn = sqlite3.connect("sql_app.db")
    cursor = conn.cursor()
    
    users = ["juan_perez", "maria_gomez", "carlos_test", "lucia_random", "marcos_prode"]
    password = "golazo2026"
    
    for u in users:
        try:
            cursor.execute("INSERT INTO usuarios (username, password, puntos_totales) VALUES (?, ?, ?)", (u, password, 0))
            print(f"Usuario '{u}' creado.")
        except sqlite3.IntegrityError:
            print(f"Usuario '{u}' ya existe.")
            
    conn.commit()
    conn.close()
    print("Proceso finalizado.")

if __name__ == "__main__":
    create_users()
