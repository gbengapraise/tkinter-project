import tkinter as tk
import random
import string

def generate_password():
    length = int(entry.get())
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    label.config(text=password)

root = tk.Tk()
root.geometry("400x400")

tk.Label(root, text="Password Length:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()
label = tk.Label(root, text="", font=('Arial', 20))
label.pack()

root.mainloop()