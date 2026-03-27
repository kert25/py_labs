import tkinter as tk
from datetime import datetime


def send_message():
    message = entry.get().strip()
    if message:
        timestamp = datetime.now().strftime("%H:%M")
        chat_area.insert(tk.END, f"[{timestamp}] Вы: {message}\n")
        entry.delete(0, tk.END)
        chat_area.see(tk.END)


root = tk.Tk()
root.title("Локальный чат")
root.geometry("400x400")

chat_area = tk.Text(root, height=20, width=50, state=tk.NORMAL)
chat_area.pack(padx=10, pady=10)

frame = tk.Frame(root)
frame.pack(padx=10, pady=5, fill=tk.X)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

button = tk.Button(frame, text="Отправить", command=send_message)
button.pack(side=tk.RIGHT, padx=(5, 0))

entry.bind("<Return>", lambda event: send_message())

root.mainloop()
