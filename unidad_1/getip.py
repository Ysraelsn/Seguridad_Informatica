'''
Este código es un script en Python que toma una URL
proporcionada por el usuario y convierte esa URL en su dirección IP 
usando la función de resolución de nombres de dominio (DNS) socket.gethostbyname.

Desarrollado por Jaime Israel Sánchez Nava.
'''
import msvcrt
import socket
import sys
import argparse
from msvcrt import getch

parse = argparse.ArgumentParser()
parse.add_argument('-t','--target',help='Ingresa la URL sin HTTP')
parse = parse.parse_args()

def getIP(url):
    try:
        ip = socket.gethostbyname(url)
        print(f'La dirección IP de {url} es: {ip}')
    except:
        print('No se pudo obtener la IP.')

def main():
    if parse.target:
        getIP(parse.target)
        
    else:
        print('Ingrese una dirección sin HTTP')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        print("Presiona cualquier tecla para salir...")
        msvcrt.getch()