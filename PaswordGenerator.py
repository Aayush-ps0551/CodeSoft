import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        all_chars = lower + upper + digits + symbols

        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols),
        ]

        password += random.choices(all_chars, k=length - 4)
        random.shuffle(password)

        entry_result.delete(0, tk.END)
        entry_result.insert(0, ''.join(password))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.config(bg="#f0f0f0")

label_intro = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
label_intro.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

label_length = tk.Label(frame, text="Password Length:", font=("Arial", 12), bg="#f0f0f0")
label_length.grid(row=0, column=0, padx=5)

entry_length = tk.Entry(frame, width=10)
entry_length.grid(row=0, column=1, padx=5)

btn_generate = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_generate.pack(pady=10)

entry_result = tk.Entry(root, width=35, font=("Arial", 12), justify="center")
entry_result.pack(pady=5)

root.mainloop()
