import tkinter as tk

score = 0


def click():
    global score
    score += 1
    label_score.config(text=f"Счёт: {score}")


def reset():
    global score
    score = 0
    label_score.config(text=f"Счёт: {score}")


root = tk.Tk()
root.title("Кликер")
root.geometry("300x200")

label_score = tk.Label(root, text="Счёт: 0", font=("Arial", 24))
label_score.pack(pady=20)

button_click = tk.Button(root, text="Клик!", font=("Arial", 16), command=click)
button_click.pack(pady=5)

button_reset = tk.Button(root, text="Сброс", font=("Arial", 12), command=reset)
button_reset.pack(pady=5)

root.mainloop()
