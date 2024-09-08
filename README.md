### README

# Sistema de Gestión de Notas en Python con Tkinder y SQLite3

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando **Tkinter** y **SQLite3**. Su principal propósito es permitir la gestión y cálculo de promedios de notas, con funcionalidades como agregar, editar y eliminar registros. La interfaz gráfica es moderna, interactiva y fácilmente extensible.

## Funcionalidades

- **Cálculo de Promedio**: Introduce las notas de un estudiante y calcula el promedio de manera automática.
- **Gestión de Registros**: Los datos pueden ser agregados, editados o eliminados. Estos se almacenan en una base de datos SQLite para su persistencia.
- **Interfaz Gráfica**: Una interfaz intuitiva y sencilla de usar con campos de texto, botones y una tabla interactiva.
- **Tabla de Visualización**: Visualiza todos los registros en una tabla, permitiendo seleccionar y editar entradas.
- **Interactividad**: Los botones cambian de color al pasar el cursor para mejorar la experiencia del usuario.

## Requisitos

- **Python 3.x**
- **Tkinter** (instalado por defecto en la mayoría de distribuciones de Python)
- **SQLite3** (instalado por defecto con Python)

## Instalación

1. Clona este repositorio o descarga los archivos:
   ```bash
   git clone https://github.com/Argon69/GUIPromedioTkinder.git
   cd GUIPromedioTkinder
   ```

2. Asegúrate de tener instaladas las dependencias necesarias. En la mayoría de los casos, **Tkinter** y **SQLite** vienen preinstalados con Python. Si no es así, instálalos usando tu gestor de paquetes:
   ```bash
   sudo apt-get install python3-tk
   ```

3. Ejecuta la aplicación:
   ```bash
   python3 promedio.py
   ```

## Estructura del Proyecto

- **Base de Datos**: Utiliza SQLite para almacenar los registros de los estudiantes y sus notas.
- **Interfaz Gráfica**: Creada con Tkinter. Todos los elementos como entradas de texto, botones, y tablas están diseñados para ofrecer una experiencia de usuario sencilla.
- **Lógica de Negocios**: Implementa funciones para agregar, editar y eliminar registros de la base de datos, así como para calcular promedios.

### Explicación del Código

- **Base de Datos**: 
  - La función `crear_bd()` crea la tabla si no existe.
  - Las funciones `insertar_datos()`, `actualizar_datos()` y `borrar_registro()` permiten gestionar los registros en la base de datos.
  
- **Interfaz Gráfica**:
  - La ventana principal está definida en `ventana_principal()`, donde se crean las etiquetas, campos de texto, botones y la tabla para visualizar los registros.
  - Se usan `ttk.Treeview` para la tabla y `tk.Entry` para los campos de texto.
  
- **Calcular Promedio**: 
  - La función `calcular_promedio()` toma las cuatro notas ingresadas y devuelve su promedio, mostrando el resultado en la interfaz.
  
- **Gestión de Registros**:
  - La función `seleccionar_registro()` permite al usuario seleccionar un registro de la tabla para editar o borrar.
  - `editar_registro()` actualiza los datos del registro seleccionado, mientras que `borrar_registro()` lo elimina.

### Uso de la Aplicación

1. **Agregar Notas**: Introduce el nombre del estudiante y sus cuatro notas, luego presiona "Calcular Promedio".
2. **Editar Registro**: Selecciona un registro en la tabla y edita sus valores en los campos. Presiona el botón "Editar" para guardar los cambios.
3. **Eliminar Registro**: Selecciona un registro y presiona el botón "Borrar" para eliminarlo de la base de datos.
   
## Personalización

- **Colores y Estilo**: Puedes modificar los colores de fondo y texto de la interfaz cambiando las variables `color_fondo`, `color_boton`, `color_texto`, etc.
- **Funcionalidad**: El código está estructurado de forma modular, por lo que es fácil agregar nuevas características como nuevas columnas o reportes.

## Contribución

Las contribuciones son bienvenidas. Siéntete libre de hacer un **fork** del repositorio y enviar un **pull request** con mejoras o nuevas funcionalidades.

---
