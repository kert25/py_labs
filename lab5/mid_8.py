import tkinter as tk
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if filepath:
        label.config(text=f"Выбран файл: {filepath}")


root = tk.Tk()
root.title("Диалог выбора файла")
root.geometry("400x150")

button = tk.Button(root, text="Открыть файл", command=open_file)
button.pack(pady=20)

label = tk.Label(root, text="Файл не выбран")
label.pack(pady=10)

root.mainloop()
