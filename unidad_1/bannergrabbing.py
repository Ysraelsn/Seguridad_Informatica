'''
Programa para encontrar subdominios de un sitio
Explicar que hace este script.
Desarrollado por Jaime Israel Sánchez Nava.
'''

import socket
import sys
import argparse

def banner_grabbing(dom,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((dom, int(port)))
        sock.settimeout(5)
        banner = sock.recv(1024)
        
        print(f'Banner recibido desde {dom}:{port}:\n{banner.decode().strip()}')
        
    except socket.timeout:
        print(f'Timeout: No se pudo recibir el banner desde {dom}:{port}.')
    finally:
        sock.close()

if __name__=="__main__":
    if len(sys.argv) !=5:
        print('Uso: py bannergrabbing.py -t <dom> -p <port>')
        sys.exit(1)
    dom = ''
    port = 0
    
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-t':
            dom = sys.argv[i+1]
        elif sys.argv[i] =='-p':
            port = sys.argv[i+1]
            
    banner_grabbing(dom,port)
    
    sys.exit(1)