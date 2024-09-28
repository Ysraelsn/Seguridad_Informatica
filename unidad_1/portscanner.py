'''
Este código es un escáner de puertos que intenta conectarse 
a varios puertos en un dominio objetivo especificado por el usuario.
El script lee los números de puerto desde un archivo llamado puertos.txt 
y verifica si están abiertos o cerrados en el dominio objetivo.

Desarrollado por Jaime Israel Sánchez Nava.
'''

import socket
import sys
import argparse
from os import path
import msvcrt

#conf
parser = argparse.ArgumentParser(description="Script para buscar puertos.")
parser.add_argument('-t', '--target', help='Indica el dominio objetivo', required=True)
args = parser.parse_args()

def main():
    if path.exists('puertos.txt'):
        with open('puertos.txt', 'r') as wordlist:
            puertos = wordlist.read().splitlines()

        if not puertos:
            print("No hay nada")
            return

        for puerto in puertos:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            resultado = s.connect_ex((args.target, int(puerto)))
            if resultado == 0:
                print(f"El puerto: {puerto} esta abierto y vulnerable")

            s.close()
            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        print("Presiona cualquier tecla para salir...")
        msvcrt.getch()
