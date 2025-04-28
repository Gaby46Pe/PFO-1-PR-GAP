import socket	
# Función para conectarse al servidor	
def conectar_al_servidor(host='127.0.0.1', port=5000):	
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
    try:	
        sock.connect((host, port))	
        print(f"Conectado al servidor en {host}:{port}")	
    except ConnectionRefusedError:	
        print("No se pudo conectar al servidor. Asegúrate de que esté en ejecución.")	
        sock = None	
    return sock	
if __name__ == '__main__':	
    sock = conectar_al_servidor()	
    if sock:	
        while True:	
            mensaje = input("Escribe tu mensaje (o 'éxito' para terminar): ")	
            if mensaje.lower() == 'éxito':	
                break	
            try:	
                sock.sendall(mensaje.encode('utf-8'))	
                respuesta = sock.recv(1024).decode('utf-8')	
                print(f"Respuesta del servidor: {respuesta}")	
            except Exception as e:	
                print(f"Error en la comunicación: {e}")	
                break	
        sock.close()	
        print("Conexión cerrada.")	
