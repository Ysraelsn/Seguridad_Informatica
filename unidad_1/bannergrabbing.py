'''
Este código realiza banner grabbing, 
que es una técnica utilizada para obtener información del servicio 
que se está ejecutando en un puerto específico de un servidor. 
Esto puede revelar detalles útiles como el software 
y la versión que está operando en ese puerto.

Desarrollado por Jaime Israel Sánchez Nava.
'''

import socket
import sys
import argparse
import msvcrt

def banner_grabbing(dom,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((dom, int(port)))
        banner = sock.recv(1024)
        
        print(f'Banner recibido desde {dom}:{port}:\n{banner.decode().strip()}')
        
    except socket.timeout:
        print(f'Timeout: No se pudo recibir el banner desde {dom}:{port}.')
    except socket.error as e:
        print(f'Error de conexión a {dom}:{port} - {e}')
    finally:
        sock.close()

if __name__ == "__main__":
    # Configuración del argumento para el dominio objetivo y el puerto
    parser = argparse.ArgumentParser(description="Script para obtener el banner de un servicio.")
    parser.add_argument('-t', '--target', help='Indica el dominio objetivo', required=True)
    parser.add_argument('-p', '--port', help='Indica el puerto del servicio', type=int, required=True)
    
    args = parser.parse_args()
    
    try:
        banner_grabbing(args.target, args.port)
    except KeyboardInterrupt:
        print("\nEscaneo interrumpido por el usuario.")
        sys.exit()
    finally:
        print("Presiona cualquier tecla para salir...")
        msvcrt.getch()  # Pausa para que no cierre inmediatamente la consola