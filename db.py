import sqlite3	
def crear_base_datos():	
    # Conectamos con la base de datos (se crea si no existe)	
    conn = sqlite3.connect('chat.db')	
    cursor = conn.cursor()	
    # Creamos la tabla si no existe	
    cursor.execute('''	
        CREATE TABLE IF NOT EXISTS mensajes (	
            id INTEGER PRIMARY KEY AUTOINCREMENT,	
            contenido TEXT NOT NULL,	
            fecha_envio TEXT NOT NULL,	
            ip_cliente TEXT NOT NULL	
        )	
    ''')	
    conn.commit()	
    conn.close()	
if __name__ == '__main__':	
    crear_base_datos()	
