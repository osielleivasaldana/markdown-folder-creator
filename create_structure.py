import os

def create_structure_from_markdown(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    path_stack = []
    base_directory = ''
    is_base_directory_set = False

    for line in lines:
        line = line.rstrip('\n').rstrip()
        if not line.strip() or line.startswith('```') or line.startswith('---'):
            continue

        # Remover caracteres de dibujo de línea y espacios iniciales
        line_clean = line.lstrip('│├└─ ').strip()
        # Calcular el nivel de indentación basado en espacios o caracteres de dibujo
        indent = len(line) - len(line.lstrip(' │├└─'))
        indent_level = indent // 4  # Asumiendo indentación de 4 espacios

        # Actualizar la pila de rutas según el nivel de indentación
        while len(path_stack) > indent_level:
            path_stack.pop()

        # Verificar si es un directorio o un archivo
        if line_clean.endswith('/'):
            # Es un directorio
            dir_name = line_clean.rstrip('/')
            if not is_base_directory_set:
                # Establecer el directorio base
                base_directory = dir_name
                is_base_directory_set = True
                path_stack.append(base_directory)
                dir_path = os.path.join(*path_stack)
            else:
                path_stack.append(dir_name)
                dir_path = os.path.join(*path_stack)
            os.makedirs(dir_path, exist_ok=True)
        else:
            # Es un archivo
            file_name = line_clean
            file_path = os.path.join(*path_stack, file_name)
            dir_name = os.path.dirname(file_path)
            # Crear el directorio si no existe y dir_name no está vacío
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)
            # Crear el archivo vacío
            with open(file_path, 'w', encoding='utf-8') as f:
                pass

    print("Estructura de carpetas y archivos creada exitosamente.")

create_structure_from_markdown('estructura.md')
