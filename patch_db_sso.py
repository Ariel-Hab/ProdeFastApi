import sqlite3
import os

def check_and_add_column(cursor, table_name, column_name, column_type):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]
    if column_name not in columns:
        print(f"Adding '{column_name}' column to '{table_name}' table...")
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
        return True
    return False

def patch_db():
    db_path = "sql_app.db"
    if not os.path.exists(db_path):
        print(f"Database file '{db_path}' not found.")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Check for external_id
        if check_and_add_column(cursor, "usuarios", "external_id", "VARCHAR"):
             try:
                 cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS ix_usuarios_external_id ON usuarios (external_id)")
                 print("Created index for external_id.")
             except Exception as e:
                 print(f"Error creating index: {e}")
        else:
             print("Column 'external_id' already exists.")

        conn.commit()
        print("Database patched successfully!")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    patch_db()
