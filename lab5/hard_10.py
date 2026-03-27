import tkinter as tk
from datetime import datetime


def send_message():
    message = entry.get().strip()
    if message:
        timestamp = datetime.now().strftime("%H:%M")
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"[{timestamp}] {message}\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)
        entry.delete(0, tk.END)


root = tk.Tk()
root.title("Локальный чат")
root.geometry("500x600")
root.minsize(400, 300)

chat_area = tk.Text(
    root, wrap=tk.WORD, state=tk.DISABLED,
    font=("Arial", 11)
)
chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 5))
entry.focus()

button = tk.Button(
    frame, text="Отправить", font=("Arial", 12), command=send_message,
    bg="#25d366", fg="white"
)
button.pack(side=tk.RIGHT)

entry.bind("<Return>", lambda event: send_message())
root.mainloop()
