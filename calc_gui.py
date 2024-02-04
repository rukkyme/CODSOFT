import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    #user enters number and it checks for the validity of numbers and operator
    try:
        number1 = float(entry_number1.get())
        number2 = float(entry_number2.get())
        operator = operator_var.get()

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "/":
            result = number1 / number2
        else:
            result = "Invalid operator"
#if valid it prints result
        result_label.config(text=f"Result: {result}")
#if invalid it gives a pop up message
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear():
    entry_number1.delete(0, tk.END)
    entry_number2.delete(0, tk.END)
    result_label.config(text="Result:")

# GUI setup
root = tk.Tk()
root.title("D'Noj Calculator")
root.geometry("700x500")
root.configure(bg='teal')


# Entry for the first number
entry_number1 = ttk.Entry(root, width=20, font=('Arial', 14))  # Adjust width and font size
entry_number1.grid(row=1, column=0, padx=20, pady=20)

# Combobox for the operator
operator_var = tk.StringVar()
operator_combobox = ttk.Combobox(root, textvariable=operator_var, values=["+", "-", "*", "/"])
operator_combobox.grid(row=1, column=1, padx=20, pady=20)
operator_combobox.set("+")

# Entry for the second number
entry_number2 = ttk.Entry(root, width=20, font=('Arial', 14))  # Adjust width and font size
entry_number2.grid(row=1, column=2, padx=20, pady=20)

# Button to perform calculation
calculate_button = ttk.Button(root, width=40, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=5, pady=100)

# Button to clear
clear_button = ttk.Button(root, width=30, text="Clear", command=clear)
clear_button.grid(row=3, column=0, columnspan=3, pady=20)

# Label to display the result
result_label = ttk.Label(root,width=30, text="Result:")
result_label.grid(row=4, column=0, columnspan=6, pady=20)

root.mainloop()
