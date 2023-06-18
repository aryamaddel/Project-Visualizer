import os

def print_directory_contents(path, level=0, exclude_dirs=[]):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            if level == 0:
                print('    ' * level + child)
            else:
                print('    ' * level + '|-' + child)
            if child not in exclude_dirs:
                print_directory_contents(child_path, level + 1, exclude_dirs)
        else:
            if level == 0:
                print('    ' * level + os.path.basename(child_path))
            else:
                print('    ' * level + '|-' + os.path.basename(child_path))

folder_path = "C:/Users/Arya/Github/Tatsumaki-Bot"
exclude_dirs = ['node_modules', 'venv', '.git', '__pycache__']
print_directory_contents(folder_path, 0, exclude_dirs)