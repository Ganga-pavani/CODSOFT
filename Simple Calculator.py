import tkinter as tk
import math
def evaluate_expression():
    try:
        expression = entry.get()
        expression = expression.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
        result = eval(expression)
        result_label.config(text=f"Result: {result:.4f}")
    except Exception as e:
        result_label.config(text="Error")


root = tk.Tk()
root.title("Simple Calculator")


entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sin', 'cos', 'tan'
]

row_val = 1
col_val = 0

for button in buttons:
    if button in ('sin', 'cos', 'tan'):
        tk.Button(root, text=button, width=5, height=2, command=lambda b=button: entry.insert(tk.END, f"{b}(")).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

equal_button = tk.Button(root, text="=", width=5, height=2, command=evaluate_expression)
equal_button.grid(row=5, column=3)

clear_button = tk.Button(root, text="Clear", width=5, height=2, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=5, column=0, columnspan=3)

result_label = tk.Label(root, text="", width=20)
result_label.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
