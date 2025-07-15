import tkinter as tk
from tkinter import messagebox
import json
import os


TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "[✔] " if task['completed'] else "[✖] "
        listbox.insert(tk.END, status + task['title'])

def add_task():
    title = entry.get()
    if title:
        tasks.append({'title': title, 'completed': False})
        save_tasks(tasks)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task.")

def mark_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['completed'] = True
        save_tasks(tasks)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        save_tasks(tasks)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a task.")


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = load_tasks()

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

tk.Button(root, text="Mark as Completed", command=mark_completed).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

update_listbox()
root.mainloop()
