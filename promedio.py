import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Función para crear la base de datos y tabla si no existe
def crear_bd():
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nota1 REAL NOT NULL,
            nota2 REAL NOT NULL,
            nota3 REAL NOT NULL,
            nota4 REAL NOT NULL,
            promedio REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función para insertar datos en la base de datos
def insertar_datos(nombre, nota1, nota2, nota3, nota4, promedio):
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO estudiantes (nombre, nota1, nota2, nota3, nota4, promedio)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombre, nota1, nota2, nota3, nota4, promedio))
    conn.commit()
    conn.close()

# Función para actualizar los datos en la base de datos
def actualizar_datos(id_estudiante, nombre, nota1, nota2, nota3, nota4, promedio):
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE estudiantes
        SET nombre = ?, nota1 = ?, nota2 = ?, nota3 = ?, nota4 = ?, promedio = ?
        WHERE id = ?
    ''', (nombre, nota1, nota2, nota3, nota4, promedio, id_estudiante))
    conn.commit()
    conn.close()

# Función para borrar un registro de la base de datos
def borrar_datos(id_estudiante):
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM estudiantes WHERE id = ?', (id_estudiante,))
    conn.commit()
    conn.close()

# Función para calcular el promedio y guardar en la base de datos
def calcular_promedio():
    nombre = entry_nombre.get()
    try:
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())
        nota4 = float(entry_nota4.get())
        promedio = (nota1 + nota2 + nota3 + nota4) / 4
        label_resultado.config(text=f"Promedio: {promedio:.2f}")

        # Insertar en la base de datos
        insertar_datos(nombre, nota1, nota2, nota3, nota4, promedio)
        messagebox.showinfo("Éxito", "Datos guardados correctamente")

        # Actualizar la tabla
        actualizar_tabla()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

# Función para limpiar las entradas
def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_nota1.delete(0, tk.END)
    entry_nota2.delete(0, tk.END)
    entry_nota3.delete(0, tk.END)
    entry_nota4.delete(0, tk.END)
    label_resultado.config(text="Promedio:")

# Función para actualizar la tabla con los datos de la base de datos
def actualizar_tabla():
    for i in tabla.get_children():
        tabla.delete(i)  # Limpiar la tabla
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, nota1, nota2, nota3, nota4, promedio FROM estudiantes')
    rows = cursor.fetchall()
    for row in rows:
        tabla.insert("", tk.END, values=row)
    conn.close()

# Función para seleccionar un registro en la tabla
def seleccionar_registro(event):
    try:
        selected_item = tabla.selection()[0]  # Obtener el ID del registro seleccionado
        valores = tabla.item(selected_item, 'values')
        
        # Cargar los valores en las entradas
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, valores[1])
        entry_nota1.delete(0, tk.END)
        entry_nota1.insert(0, valores[2])
        entry_nota2.delete(0, tk.END)
        entry_nota2.insert(0, valores[3])
        entry_nota3.delete(0, tk.END)
        entry_nota3.insert(0, valores[4])
        entry_nota4.delete(0, tk.END)
        entry_nota4.insert(0, valores[5])
        
        global id_estudiante_seleccionado
        id_estudiante_seleccionado = valores[0]  # Guardar el ID del estudiante seleccionado
    except IndexError:
        pass

# Función para editar el registro seleccionado
def editar_registro():
    nombre = entry_nombre.get()
    try:
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())
        nota4 = float(entry_nota4.get())
        promedio = (nota1 + nota2 + nota3 + nota4) / 4

        # Actualizar los datos en la base de datos
        actualizar_datos(id_estudiante_seleccionado, nombre, nota1, nota2, nota3, nota4, promedio)
        messagebox.showinfo("Éxito", "Registro actualizado correctamente")

        # Limpiar las entradas y actualizar la tabla
        limpiar()
        actualizar_tabla()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

# Función para borrar el registro seleccionado
def borrar_registro():
    try:
        borrar_datos(id_estudiante_seleccionado)
        messagebox.showinfo("Éxito", "Registro eliminado correctamente")

        # Limpiar las entradas y actualizar la tabla
        limpiar()
        actualizar_tabla()
    except NameError:
        messagebox.showerror("Error", "Por favor seleccione un registro para eliminar")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Reporte de Notas")
ventana.geometry("600x600")
ventana.configure(bg="#2E4053")

# Definir colores
color_fondo = "#2E4053"
color_texto = "#F7F9F9"
color_entry = "#D5DBDB"
color_boton = "#5DADE2"
color_boton_hover = "#5499C7"
color_resultado = "#48C9B0"

# Estilos comunes
fuente_entrada = ("Arial", 12)
fuente_texto = ("Arial", 12, "bold")

# Cambiar color del botón al pasar el cursor
def on_enter(e):
    e.widget['background'] = color_boton_hover

def on_leave(e):
    e.widget['background'] = color_boton

# Etiqueta y entrada para el nombre del estudiante
label_nombre = tk.Label(ventana, text="Nombre del Estudiante:", bg=color_fondo, fg=color_texto, font=fuente_texto)
label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nombre = tk.Entry(ventana, bg=color_entry, font=fuente_entrada)
entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Entradas para las notas
label_nota1 = tk.Label(ventana, text="Nota 1:", bg=color_fondo, fg=color_texto, font=fuente_texto)
label_nota1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nota1 = tk.Entry(ventana, bg=color_entry, font=fuente_entrada)
entry_nota1.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

label_nota2 = tk.Label(ventana, text="Nota 2:", bg=color_fondo, fg=color_texto, font=fuente_texto)
label_nota2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_nota2 = tk.Entry(ventana, bg=color_entry, font=fuente_entrada)
entry_nota2.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

label_nota3 = tk.Label(ventana, text="Nota 3:", bg=color_fondo, fg=color_texto, font=fuente_texto)
label_nota3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_nota3 = tk.Entry(ventana, bg=color_entry, font=fuente_entrada)
entry_nota3.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

label_nota4 = tk.Label(ventana, text="Nota 4:", bg=color_fondo, fg=color_texto, font=fuente_texto)
label_nota4.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_nota4 = tk.Entry(ventana, bg=color_entry, font=fuente_entrada)
entry_nota4.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Mostrar el promedio
label_resultado = tk.Label(ventana, text="Promedio:", bg=color_fondo, fg=color_resultado, font=fuente_texto)
label_resultado.grid(row=5, column=1, padx=10, pady=10)

# Botón para calcular el promedio
boton_calcular = tk.Button(ventana, text="Calcular Promedio", bg=color_boton, fg=color_texto, font=fuente_texto, command=calcular_promedio)
boton_calcular.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
boton_calcular.bind("<Enter>", on_enter)
boton_calcular.bind("<Leave>", on_leave)

# Botón para limpiar las entradas
boton_limpiar = tk.Button(ventana, text="Limpiar", bg=color_boton, fg=color_texto, font=fuente_texto, command=limpiar)
boton_limpiar.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
boton_limpiar.bind("<Enter>", on_enter)
boton_limpiar.bind("<Leave>", on_leave)

# Tabla de reportes
tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Promedio"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Nota 1", text="Nota 1")
tabla.heading("Nota 2", text="Nota 2")
tabla.heading("Nota 3", text="Nota 3")
tabla.heading("Nota 4", text="Nota 4")
tabla.heading("Promedio", text="Promedio")
tabla.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Scrollbar para la tabla
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
scrollbar.grid(row=7, column=2, sticky="ns")
tabla.configure(yscrollcommand=scrollbar.set)

# Botón para editar un registro
boton_editar = tk.Button(ventana, text="Editar", bg=color_boton, fg=color_texto, font=fuente_texto, command=editar_registro)
boton_editar.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
boton_editar.bind("<Enter>", on_enter)
boton_editar.bind("<Leave>", on_leave)

# Botón para borrar un registro
boton_borrar = tk.Button(ventana, text="Borrar", bg=color_boton, fg=color_texto, font=fuente_texto, command=borrar_registro)
boton_borrar.grid(row=8, column=1, padx=10, pady=10, sticky="ew")
boton_borrar.bind("<Enter>", on_enter)
boton_borrar.bind("<Leave>", on_leave)

# Selección de un registro en la tabla
tabla.bind("<<TreeviewSelect>>", seleccionar_registro)

# Hacer que la ventana sea responsive
ventana.grid_rowconfigure(7, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Crear la base de datos y tabla si no existen
crear_bd()

# Actualizar la tabla con los datos existentes
actualizar_tabla()

ventana.mainloop()
