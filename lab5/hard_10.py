import tkinter as tk
from datetime import datetime


def send_message():
    message = entry.get().strip()
    if message:
        timestamp = datetime.now().strftime("%H:%M")
        chat_area.config(state=tk.NORMAL)

        chat_area.insert(tk.END, f"{message}\n", "message")
        chat_area.insert(tk.END, f"{timestamp}\n\n", "time")

        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)
        entry.delete(0, tk.END)


root = tk.Tk()
root.title("Локальный чат")
root.geometry("400x500")
root.configure(bg="#e5ddd5")

chat_area = tk.Text(
    root, wrap=tk.WORD, state=tk.DISABLED, bg="#e5ddd5",
    font=("Arial", 11), relief=tk.FLAT, padx=10, pady=10
)
chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

chat_area.tag_configure(
    "message", justify=tk.RIGHT, background="#dcf8c6",
    relief=tk.FLAT, lmargin1=100, lmargin2=100,
    rmargin=10, spacing3=2, font=("Arial", 11)
)
chat_area.tag_configure(
    "time", justify=tk.RIGHT, foreground="#667781",
    font=("Arial", 8), spacing3=10
)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 5))

button = tk.Button(
    frame, text="➤", font=("Arial", 14), command=send_message,
    bg="#25d366", fg="white", relief=tk.FLAT, width=3
)
button.pack(side=tk.RIGHT)

entry.bind("<Return>", lambda event: send_message())

root.mainloop()
