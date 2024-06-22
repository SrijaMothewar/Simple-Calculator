import tkinter as tk
from tkinter import messagebox
import math

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Math error", "Division by zero is not allowed")
        else:
            result = float(entry1.get()) / float(entry2.get())
            result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def square_root():
    try:
        result = math.sqrt(float(entry1.get()))
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def exponentiate():
    try:
        result = float(entry1.get()) ** float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

app = tk.Tk()
app.title("Simple Calculator")

tk.Label(app, text="First Number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Second Number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=1, padx=10, pady=10)

result_var = tk.StringVar()
tk.Label(app, text="Result:").grid(row=2, column=0, padx=10, pady=10)
result_label = tk.Label(app, textvariable=result_var)
result_label.grid(row=2, column=1, padx=10, pady=10)

tk.Button(app, text="Add", command=add).grid(row=0, column=2, padx=10, pady=10)
tk.Button(app, text="Subtract", command=subtract).grid(row=1, column=2, padx=10, pady=10)
tk.Button(app, text="Multiply", command=multiply).grid(row=0, column=3, padx=10, pady=10)
tk.Button(app, text="Divide", command=divide).grid(row=1, column=3, padx=10, pady=10)
tk.Button(app, text="Square Root", command=square_root).grid(row=2, column=2, padx=10, pady=10)
tk.Button(app, text="Exponentiate", command=exponentiate).grid(row=2, column=3, padx=10, pady=10)

app.mainloop()
