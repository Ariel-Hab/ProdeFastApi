import sqlite3
import os

def patch_db_premios():
    db_path = "sql_app.db"
    if not os.path.exists(db_path):
        print(f"Database file '{db_path}' not found.")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create table premios if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS premios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR,
                descripcion VARCHAR,
                puntos_requeridos INTEGER DEFAULT 0,
                imagen_url VARCHAR,
                orden INTEGER DEFAULT 0
            )
        """)
        
        # Create an index for faster ordering
        cursor.execute("CREATE INDEX IF NOT EXISTS ix_premios_orden ON premios (orden)")
        
        conn.commit()
        print("Table 'premios' ensured.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    patch_db_premios()
