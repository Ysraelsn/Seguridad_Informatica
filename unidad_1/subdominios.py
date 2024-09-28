'''
Programa para encontrar subdominios de un sitio
Explicar que hace este script.
Desarrollado por Jaime Israel Sánchez Nava.
'''
import msvcrt
import requests
from os import path 
import argparse
import sys
from msvcrt import getch

parser = argparse.ArgumentParser()

# print(f"{parse}\n\n")
parser.add_argument('-t','--target',help='Indica el dominio de la víctima')

parser = parser.parse_args()
# print(parse)
'''
Este es un comentario multilínea
'''

def main():
    if parser.target:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt','r')
            wordlist = wordlist.read().split('\n')
            
            for subdominio in wordlist:
                url = "http://" + subdominio + "." + parser.target
                #print(url)
                
                try:
                    requests.get(url, timeout=3)
                    
                except requests.ConnectionError: pass
                else: print("Se encontró un subdominio:" + url)

             
            for subdominio in wordlist:
                url = "https://" + subdominio + "." + parser.target
                #print(url)
                
                try:
                    requests.get(url, timeout=3)
                    
                except requests.ConnectionError: pass
                else: print("Se encontró un subdominio:" + url)
                
        else: print('No se encontró el archivo que contiene los subdominios a buscar')
    else: print("No hay victima")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        print("Presiona cualquier tecla para salir...")
        msvcrt.getch()