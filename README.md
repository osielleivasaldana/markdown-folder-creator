# Generador de Estructura de Proyecto desde Markdown

Este repositorio contiene un script en Python que permite generar la estructura de directorios y archivos de un proyecto a partir de un archivo Markdown que describe dicha estructura. Esto es útil para inicializar rápidamente proyectos con una configuración específica sin tener que crear manualmente cada carpeta y archivo.

## **Tabla de Contenidos**

- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo de Archivo Markdown](#ejemplo-de-archivo-markdown)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Notas Adicionales](#notas-adicionales)
- [Licencia](#licencia)

## **Requisitos Previos**

- **Python 3.6 o superior** instalado en tu sistema.
- Conocimientos básicos de línea de comandos.

## **Instalación**

1. **Clona este repositorio** o descarga el archivo `create_structure.py` en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git

2. cd tu_repositorio

## **Uso**

El script create_structure.py lee un archivo Markdown que describe la estructura del proyecto y crea las carpetas y archivos correspondientes.

Pasos para ejecutar el script:

Prepara el archivo Markdown que describe la estructura de tu proyecto. Por defecto, el script busca un archivo llamado estructura.md en el mismo directorio.

Verifica que el archivo Markdown esté correctamente formateado y guardado con codificación UTF-8.

## **Ejemplo de Uso**
Sigue estos pasos para utilizar el script con el archivo de ejemplo proporcionado:

Crea el archivo estructura.md en el mismo directorio que create_structure.py y copia el contenido del ejemplo anterior.

Ejecuta el script en la línea de comandos:
  
 `python create_structure.py`
  



Si deseas especificar un archivo Markdown diferente o un directorio base distinto, puedes modificar el script según tus necesidades.

## **Ejemplo de Archivo Markdown**

A continuación se muestra un ejemplo de cómo se debería ver tu archivo estructura.md


```
tu_proyecto/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── question.py
│   │   └── option.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── question.py
│   │   └── option.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── question.py
│   │   └── option.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── questions.py
│   │       └── options.py
├── main.py
├── requirements.txt
├── .env
```



## **Notas Adicionales**

Personalización del Script:

Si deseas cambiar el nombre del archivo Markdown o especificar un directorio base diferente, puedes modificar el script create_structure.py

`# Para cambiar el archivo Markdown de entrada:
create_structure_from_markdown('mi_estructura.md')

# Para especificar el directorio base manualmente:
create_structure_from_markdown('estructura.md', 'mi_proyecto')
`
Manejo de Errores

Asegúrate de que el archivo Markdown esté correctamente formateado y que no contenga errores de sintaxis. Si el script encuentra un problema, imprimirá un mensaje de error en la consola.

Compatibilidad:

El script ha sido probado en sistemas Windows, macOS y Linux. Se requiere Python 3.6 o superior.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
