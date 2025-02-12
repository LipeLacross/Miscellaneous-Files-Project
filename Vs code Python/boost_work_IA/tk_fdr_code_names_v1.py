import os

def list_directory(path, level=0, output_file=None, exclude_file=None, list_content=False):
    # Lista de pastas ignoradas
    ignored_folders = {
        '.venv', 'venv', 'env', '.idea', '.git', 'node_modules', '__pycache__', 
        'dist', 'build', '.DS_Store', '.vscode', 'target', 'out', 
        '.pytest_cache', '.mypy_cache', 'logs', 'coverage',
    }
    # Nome do arquivo atual para ser ignorado
    current_script_name = os.path.basename(__file__)

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        # Ignora arquivos e pastas ocultas
        if item.startswith('.'):
            continue

        # Ignora as pastas contidas no conjunto ignored_folders e todas as subpastas dessas pastas
        if os.path.isdir(full_path) and any(ignored in full_path for ignored in ignored_folders):
            continue

        # Processa arquivos, exceto aqueles a serem excluídos
        if os.path.isfile(full_path):
            if item == exclude_file or item == current_script_name:
                continue

            if output_file:
                output_file.write("  " * level + "|-- " + item + "\n")

            # Listar o conteúdo do arquivo, se solicitado
            if list_content and item.endswith(('.py', '.js', '.java', '.c', '.cpp', '.h', '.ipynb', '.html', '.css', '.ts', '.tsx', '.scss', '.sass', '.vue')):
                output_file.write("  " * (level + 1) + "Content:\n")
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        output_file.write("  " * (level + 2) + line)
        # Processa subdiretórios
        elif os.path.isdir(full_path):
            if output_file:
                output_file.write("  " * level + "|-- " + item + "/\n")
            list_directory(full_path, level + 1, output_file, exclude_file, list_content)

def generate_listing(directory_path, output_file_path, exclude_file_name):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        list_directory(directory_path, output_file=output_file, exclude_file=exclude_file_name)
        output_file.write("\n\nFile contents:\n\n")
        list_directory(directory_path, output_file=output_file, exclude_file=exclude_file_name, list_content=True)

directory_path = './'
output_file_path = 'directory_listing.txt'
exclude_file_name = os.path.basename(output_file_path)

generate_listing(directory_path, output_file_path, exclude_file_name)

print(f"The listing has been saved in {output_file_path}")
