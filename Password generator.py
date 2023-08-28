import tkinter as tk
import random
import string

def generate_password():
    length = 12  
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def accept_password():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")

def reset_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")


username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

accept_button = tk.Button(root, text="Accept", command=accept_password)
accept_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack()

root.mainloop()
