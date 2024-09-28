'''
Este código es un script en Python 
que usa el comando nslookup del sistema operativo 
para realizar una búsqueda de la dirección IP de un dominio 
o dirección IP objetivo proporcionada por el usuario. 
El script toma la dirección de la "víctima" 
y realiza la búsqueda de DNS, mostrando el resultado.

Desarrollado por Jaime Israel Sánchez Nava.
'''

import msvcrt
import os
import sys
import argparse
from msvcrt import getch


parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Introduce la direccion ip de la víctima')
parse = parse.parse_args()


def get_ip(target):
    try:
        res = os.system(f'nslookup {target}')
        print(res)
    except:
        print('[-] No se pudo obtener la ip')
        sys.exit(1)


def main():
    if parse.target:
        get_ip(parse.target)
    else:
        print('[-] Debes indicar la URL')
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        print("Presiona cualquier tecla para salir...")
        msvcrt.getch()
