import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def welcome():
    print("Welcome to D'Noj calculator")
    
def calculate():
    number1 = int(input("enter your first number : "))
    number2 = int(input("enter your seecond number : "))

    operation = input(''' please type the operator to be used; 
+ for additon
- for subtraction, 
* for multiplication 
/ for division)
''')


#using string format method
#For addition
    if operation == "+":
        print("{} + {} = " .format(number1, number2))
        print(number1 + number2)
#for subtraction
    elif operation == "-":
        print('{} - {} ='.format(number1, number2))
        print(number1 - number2)
#for multiplication
    elif operation == "*":
        print('{} * {} ='.format(number1, number2))
        print(number1 * number2)
#for division
    elif operation == "/":
        print('{} / {} ='.format(number1, number2))
        print(number1 / number2)

    else:
        print("no number was entered")
    
#user wishes to continue calculating after first use
def calculatecontd():
    while True:
        calc_again = input('Do you want to carry out another calculation? (y/n)\n')
        if calc_again.lower() == "y":
            calculate()
        elif calc_again.lower() == "n":
            print("Thank you for choosing D'Noj calculator")
            break 
        # If the user enters a key other than 'y' or 'n'
        else: 
            print("Error. Please enter y or n")

        
# Calling the functions
welcome()
calculate()
calculatecontd()

