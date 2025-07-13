import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

root.mainloop()