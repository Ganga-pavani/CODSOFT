import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit!")


root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
edit_button = tk.Button(root, text="Edit Task", command=edit_task)

add_button.pack()
remove_button.pack()
edit_button.pack()


listbox = tk.Listbox(root, width=40)
listbox.pack()

root.mainloop()
