'''
Programa para mostrar un menú que muestre diferentes programas de cyberseguridad

Desarrollado por Jaime Israel Sánchez Nava.
'''
import tkinter as tk
from tkinter import messagebox
import os
from msvcrt import getch
import subprocess


'''def ejecutar_opcion(opcion):
    match opcion:
        case 1:
            print('Ejecutando programa "Busqueda de Subdominios"')
            tk.messagebox.showinfo(title='Ejecución', message='Ejecutando programa "Busqueda de Subdominios')
        case 2:
            print('Ejecutando programa "Banner Grabbing"')
        case 3:
            print('Ejecutando programa "WAD"')
        case 4:
            print('Ejecutando programa "Escaneo de Puertos"')
        case 5:
            print("Saliendo del Programa")
            root.quit()    
        case _:
            print("Opción no válida")        

def seleccion_opcion(opcion):
    ejecutar_opcion(opcion)
'''

def ejecutar_opcion(archivo_py,argumentos):
    comando = ['python',archivo_py] + argumentos.split()
    try:
        
        subprocess.Popen(comando, creationflags=subprocess.CREATE_NEW_CONSOLE)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {archivo_py}: {e}")
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
    
def abrir_exe(archivo_py):
    ventana = tk.Toplevel(root)
    ventana.geometry('400x200')
    ventana.title(f'Ejecutar {archivo_py}')
    
    tk.Label(ventana, text="Ingrese los argumentos:", font=('Arial', 12)).pack(pady=10)
    tk.Label(ventana, text="Argumentos para subdominios.py: -t url", font=('Arial', 10)).pack(pady=3)
    tk.Label(ventana, text="Argumentos para bannergrabbing.py: -t url -p puerto", font=('Arial', 10)).pack(pady=3)
    entrada_argumentos = tk.Entry(ventana, width=50)
    entrada_argumentos.pack(pady=10)
    
    tk.Button(ventana, text="Ejecutar", font=('Arial', 12), 
              command=lambda: ejecutar_opcion(archivo_py, entrada_argumentos.get())).pack(pady=10)
    
# Ventana Principal    
root = tk.Tk()
root.title('Sistema de Pruebas de Cybersecurity')
root.configure(bg='#FFFFFF')
label_style = {'bg':'#FFFFFF','fg':'black','font':('Arial', 15)}

# Logo
image = tk.PhotoImage(file='logo.png')
label_img = tk.Label(image=image, padx=10, pady=15)
label_img.grid(row=0, column=0)

# Título
label_titulo = tk.Label(root, text='Sistema de Pruebas de Seguridad Informática', **label_style, justify='center')
label_titulo.grid(row=1, column=0, padx=10, pady=15)

# Menú
menu = tk.Frame(root, bg='#FFFFFF')
menu.grid(row=2, column=0, padx=20, pady=20)

opciones = [('Búsqueda de Subdominios','subdominios.py'), 
            ('Banner Grabbing','banner_grabbing.py'),
            ('WAD','wad.py'), 
            ('Escaneo de Puertos','escaneo_puertos.py'),
            ('Salir',None)]

for nombre, archivo in opciones:
    if archivo:
        boton = tk.Button(menu, text=nombre, font=('Arial', 12), width=30, command=lambda archivo=archivo: abrir_exe(archivo))
    else:
        boton=tk.Button(menu, text=nombre, font=('Arial', 12), width=30, command=root.quit)
    boton.pack(pady=5)

root.mainloop()