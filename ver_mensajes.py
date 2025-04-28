import sqlite3

def mostrar_mensajes():
    try:
        # Conecta a la base de datos
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener todos los mensajes
        cursor.execute("SELECT id, contenido, fecha_envio, ip_cliente FROM mensajes")
        mensajes = cursor.fetchall()

        # Verifica si hay mensajes
        if mensajes:
            print("Mensajes guardados en la base de datos:")
            for mensaje in mensajes:
                print(f"ID: {mensaje[0]} | Fecha: {mensaje[2]} | IP: {mensaje[3]} | Contenido: {mensaje[1]}")
        else:
            print("No hay mensajes guardados en la base de datos.")

        # Cierra la conexión
        conn.close()

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")

if __name__ == "__main__":
    mostrar_mensajes()
