import os
import tkinter as tk
from tkinter import filedialog


def print_directory_contents(path, level=0, exclude_dirs=[]):
    text = ''
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        prefix = '|-' if level > 0 else ''
        text += '    ' * level + prefix + child + '\n'
        if os.path.isdir(child_path) and child not in exclude_dirs:
            text += print_directory_contents(child_path,
                                             level + 1, exclude_dirs)
    return text


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        exclude_dirs = ['node_modules', 'venv', '.venv', '.git', '__pycache__']
        text = print_directory_contents(folder_path, 0, exclude_dirs)
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, text)
        copy_button.pack()


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_box.get("1.0", tk.END))


root = tk.Tk()
root.title("Directory Contents")

text_box = tk.Text(root)
text_box.pack()

select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack()

copy_button = tk.Button(root, text="Copy to Clipboard",
                        command=copy_to_clipboard)

root.mainloop()
