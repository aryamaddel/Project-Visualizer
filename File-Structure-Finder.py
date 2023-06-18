import os

def print_directory_contents(path, level=0, exclude_dirs=[]):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        prefix = '|-' if level > 0 else ''
        print('    ' * level + prefix + child)
        if os.path.isdir(child_path) and child not in exclude_dirs:
            print_directory_contents(child_path, level + 1, exclude_dirs)

folder_path = "C:/Users/Arya/Github/Tatsumaki-Bot"
exclude_dirs = ['node_modules', 'venv', '.git', '__pycache__']
print_directory_contents(folder_path, 0, exclude_dirs)
