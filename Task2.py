import tkinter as tk
from tkinter import messagebox

def perform_operation(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x350")
root.resizable(False, False)

tk.Label(root, text="Simple Calculator", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Enter First Number:").pack()
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

tk.Label(root, text="Choose Operation:").pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="+", width=5, command=lambda: perform_operation('+')).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="-", width=5, command=lambda: perform_operation('-')).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="*", width=5, command=lambda: perform_operation('*')).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="/", width=5, command=lambda: perform_operation('/')).grid(row=0, column=3, padx=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
