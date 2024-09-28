import tkinter as tk
import subprocess

# Función para ejecutar el archivo py   
def ejecutar_opcion(archivo_py, argumentos):
    comando = ['python', archivo_py] + argumentos.split()
    try:
        subprocess.Popen(comando, creationflags=subprocess.CREATE_NEW_CONSOLE)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {archivo_py}: {e}")
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")

#Entrada de Argumentos
def abrir_exe(archivo_py):
    ventana = tk.Toplevel(root)
    ventana.geometry('400x200')
    ventana.title(f'Ejecutando {archivo_py}')
    
    tk.Label(ventana, text="Ingrese los argumentos:", font=('Arial', 12)).pack(pady=10)
    tk.Label(ventana, text="Argumentos para subdominios.py: -t url", font=('Arial', 10)).pack(pady=3)
    tk.Label(ventana, text="Argumentos para bannergrabbing.py: -t url -p puerto", font=('Arial', 10)).pack(pady=3)
    entrada_argumentos = tk.Entry(ventana, width=50)
    entrada_argumentos.pack(pady=10)
    
    tk.Button(ventana, text="Ejecutar", font=('Arial', 12), 
              command=lambda: ejecutar_opcion(archivo_py, entrada_argumentos.get())).pack(pady=10)

# Funciones específicas para abrir cada archivo .py
def abrir_subdominios():
    abrir_exe('subdominios.py')

def abrir_banner_grabbing():
    abrir_exe('banner_grabbing.py')

def abrir_wad():
    abrir_exe('wad.py')

def abrir_escaneo_puertos():
    abrir_exe('portscanner.py')

# Ventana Principal    
root = tk.Tk()
root.title('Sistema de Pruebas de Cybersecurity')
root.configure(bg='#FFFFFF')
label_style = {'bg':'#FFFFFF','fg':'black','font':('Arial', 15)}

# Logo
image = tk.PhotoImage(file='logo.png')
label_img = tk.Label(image=image, padx=10, pady=15).grid(row=0,column=0)

# Título
label_titulo = tk.Label(root, text='Sistema de Pruebas de Seguridad Informática', **label_style, justify='center').grid(row=1, column=0, padx=10, pady=15)

# Menú
menu = tk.Frame(root, bg='#FFFFFF').grid(row=2, column=0, padx=20, pady=20)

# Botones
botones = [
    ('Búsqueda de Subdominios', abrir_subdominios),
    ('Banner Grabbing', abrir_banner_grabbing),
    ('WAD', abrir_wad),
    ('Escaneo de Puertos', abrir_escaneo_puertos),
    ('Salir', root.quit)
]

for nombre, funcion in botones:
    boton = tk.Button(menu, text=nombre, font=('Arial', 12), width=30, command=funcion).pack(pady=5)

root.mainloop()