import os

def print_directory_contents(path, level=0, exclude_dirs=[]):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print('    ' * level + child)
            if child not in exclude_dirs:
                print_directory_contents(child_path, level + 1, exclude_dirs)
        else:
            print('    ' * level + '|-' + os.path.basename(child_path))

folder_path = "C:/Users/Arya/Desktop/New folder/my-app"
exclude_dirs = ['node_modules', 'venv', '.git', '__pycache__']
print_directory_contents(folder_path, 0, exclude_dirs)