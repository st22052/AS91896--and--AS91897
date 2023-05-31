import tkinter as tk
from tkinter import ttk
import json

"""""
# Function to save data to a JSON file
def save_data():
    data = []
    for item in treeview.get_children():
        values = treeview.item(item, 'values')
        data.append(values)
    
    with open('data.json', 'w') as file:
        json.dump(data, file)

# Function to load data from a JSON file
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        for item in data:
            treeview.insert('', 'end', values=item)
    except FileNotFoundError:
        pass

# Function to add data to the table
def add_data():
    name = name_entry.get()
    age = age_entry.get()
    occupation = occupation_entry.get()
    
    if name.strip() and age.strip() and occupation.strip():
        treeview.insert('', 'end', values=(name, age, occupation))
        
        # Clear the entry fields
        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        occupation_entry.delete(0, 'end')
        
        # Save the data
        save_data()

# Create the tkinter window
window = tk.Tk()
window.title("Data Table")
window.geometry("400x300")

# Create a frame to hold the table
table_frame = tk.Frame(window)
table_frame.pack(pady=10)

# Create a Treeview widget
columns = ("Name", "Age", "Occupation")
treeview = ttk.Treeview(table_frame, columns=columns, show="headings")
treeview.pack(side="left", fill="y")

# Add scrollbars to the Treeview widget
vertical_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=treeview.yview)
vertical_scrollbar.pack(side="right", fill="y")
treeview.configure(yscrollcommand=vertical_scrollbar.set)

# Set column headings
for col in columns:
    treeview.heading(col, text=col)

# Load existing data on startup
load_data()

# Create entry fields for user input
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

occupation_label = tk.Label(window, text="Occupation:")
occupation_label.pack()
occupation_entry = tk.Entry(window)
occupation_entry.pack()

# Create a button to add data
add_button = tk.Button(window, text="Add Data", command=add_data)
add_button.pack(pady=10)

window.mainloop()
"""""