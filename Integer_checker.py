import tkinter as tk
from tkinter import ttk

def add_data():
    # Making error message if user doesn't enter an integer
    try:
        integer = int(integer_num.get())
        integer_error.config(text="Good job! That is an integer.")
    except ValueError:
        integer_error.config(text="Please enter a valid integer")
    
    

# Create the tkinter window
window = tk.Tk()
window.title("Number Integer Validation")
window.geometry("300x200")

# Create the entry field for receipt number
integer_num = tk.Entry(window)
integer_num.pack()

# Create the error label for receipt number validation
integer_error = tk.Label(window, fg="red")
integer_error.pack()

# Create the button to trigger adding data
add_button = ttk.Button(window, text="Add Data", command=add_data)
add_button.pack()

window.mainloop()