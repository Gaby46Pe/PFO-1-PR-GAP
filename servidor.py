import socket	
import sqlite3	
from datetime import datetime	
# Función para inicializar el socket TCP/IP	
def inicializar_socket(host='127.0.0.1', port=5000):	
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
    try:	
        sock.bind((host, port))	
        sock.listen(1)  # Permite una conexión en espera	
        print(f"Servidor escuchando en {host}:{port}")	
    except OSError as e:	
        print(f"Error al enlazar el socket: {e}")	
        sock.close()	
        sock = None	
    return sock	
# Función para guardar mensajes en la base de datos	
def guardar_mensaje(contenido, ip_cliente):	
    try:	
        conn = sqlite3.connect('chat.db')	
        cursor = conn.cursor()	
        fecha_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')	
        cursor.execute('''	
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)	
            VALUES (?, ?, ?)	
        ''', (contenido, fecha_envio, ip_cliente))	
        conn.commit()	
        conn.close()	
    except sqlite3.Error as e:	
        print(f"Error al guardar en la base de datos: {e}")	
# Función para aceptar conexiones y recibir mensajes	
def aceptar_conexiones(sock):	
    while True:	
        try:	
            cliente_socket, addr = sock.accept()	
            print(f"Conexión aceptada de {addr}")	
            recibir_mensajes(cliente_socket, addr)	
        except Exception as e:	
            print(f"Error al aceptar conexión: {e}")	
# Función para recibir mensajes del cliente	
def recibir_mensajes(cliente_socket, addr):	
    with cliente_socket:	
        while True:	
            try:	
                datos = cliente_socket.recv(1024)	
                if not datos:	
                    break  # Cliente desconectado	
                mensaje = datos.decode('utf-8')	
                print(f"Mensaje recibido de {addr}: {mensaje}")	
                # Guardar en la base de datos	
                guardar_mensaje(mensaje, addr[0])	
                # Enviar respuesta	
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')	
                respuesta = f"Mensaje recibido: {timestamp}"	
                cliente_socket.sendall(respuesta.encode('utf-8'))	
            except Exception as e:	
                print(f"Error en la comunicación: {e}")	
                break	
if __name__ == '__main__':	
    socket_servidor = inicializar_socket()	
    if socket_servidor:	
        aceptar_conexiones(socket_servidor)	
