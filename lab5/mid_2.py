import tkinter as tk


def show_text():
    text = entry.get()
    label_result.config(text=f"Вы ввели: {text}")


root = tk.Tk()
root.title("Текстовое поле и кнопка")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Показать текст", command=show_text)
button.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
