import tkinter as tk
from tkinter import ttk
from tkinter import *
# Create custom window
window = tk.Tk()
window.title("Julie's hire party")
window.geometry("1100x600") 
window.configure(bg="white")
window.attributes('-fullscreen',True)

# Create custom table
table_frame = tk.Frame()
table_frame.pack(pady=10)
table_frame.place(x=700,y=190)

# Adding a scroll bar for table in case user adds more data
table_scroll = Scrollbar(table_frame)
table_scroll.pack(side=RIGHT, fill=Y)

columns = ("Customer Name", "Receipt Number", "Item Hired", "Number Hired")
treeview = ttk.Treeview(table_frame, columns=columns, show="headings", height=25, yscrollcommand=table_scroll.set)
treeview.pack(pady=10)

entry_frame = ttk.Frame()
entry_frame.pack(pady=10)


# Add shapes
entry_box_bg = tk.Label(window, width=40, height=17,fg="red",bg="#213A5C")
entry_box_bg.place(x=393,y=190)

label_bg = tk.Label(window, width=40, height=17,fg="red",bg="#213A5C")
label_bg.place(x=90,y=190)

button_bg = tk.Label(window, width=84, height=10, bg="#213A5C")
button_bg.place(x=90,y=465)



#Headings for table
for col in columns:
    treeview.heading(col, text=col)


#create function to add data to the table
def add_data():
    try:
        Receipt = int(receipt_num.get())
    except ValueError:
        receipt_error.config(text="Please enter receipt number")

    Name = customer_name.get()
    Item_Hired = item_hired.get()
    Number_Hired = num_hired.get()
    
    # Validation checks
    if not Name.strip():
        customer_name_error.config(text="Name Required")
        return # Exit the function if Name is empty

    if not Item_Hired.strip():
        item_hired_error.config(text="Item Hired cannot be empty")
        return  # Exit the function if Item_Hired is empty

    if not Number_Hired.isdigit() or int(Number_Hired) < 1 or int(Number_Hired) > 500:
        num_error.config(text="1-500 Items only")
        return # Exit the function if Number_Hired is empty

    # Clear any previous error messages
    item_hired_error.config(text="")
    num_error.config(text="")
    customer_name_error.config(text="")
    # Print to terminal
    print("Name: ", Name)
    print("Item hired: ", Item_Hired)
    print("Number of items hired: ", Number_Hired)
    print("Receipt: ", Receipt)
    print("*************")

    treeview.insert("", "end", values=(Name, Receipt, Item_Hired, Number_Hired))


customer_name_error = Label(entry_box_bg, bg="yellow")
customer_name_error.place(x=50,y=35)

receipt_error = Label(entry_box_bg, bg="yellow")
receipt_error.place(x=50,y=85)

item_hired_error = Label(entry_box_bg, bg="yellow")
item_hired_error.place(x=50,y=135)

num_error = Label(entry_box_bg, bg="yellow")
num_error.place(x=50,y=185)



# Functions and buttons to delete data off of the table

#def edit():
   # Get selected item to Edit
   #selected_item = treeview.selection()[0]
   #treeview.item(selected_item, text="blub", values=(add_data))

def delete():
   # Get selected item to Delete
   selected_item = treeview.selection()[0]
   treeview.delete(selected_item)

# Function that deletes all rows of data
def delete_all():
    for add_data in treeview.get_children():
        treeview.delete(add_data)


# Add Buttons to Edit and Delete the Treeview items
#edit_btn = ttk.Button(window, text="Edit", width=23, command=edit)
#edit_btn.place(x=1000,y=440)
del_btn = ttk.Button(button_bg, text="Delete selected row", width=23, command=delete)
del_btn.place(x=350,y=100)
delete_all = ttk.Button(button_bg, text="Delete all", width=23, command=delete_all)
delete_all.place(x=100,y=100)


# Create buttons to add to table

# submit button
append_button = tk.Button(button_bg, text="Append Details & Print",font=("Arial",12,"bold"), command=add_data)
append_button.pack(padx=10,pady=300)
append_button.place(x=200,y=20)


#btn_print = tk.Button(window,text="Print Details",font=("Arial",12,"bold"), command=add_data)
#btn_print.place(x=400,y=480)

# Button to exit application
btn_exit = tk.Button(window,text="Exit application",font=("Arial",13),command=exit)
btn_exit.place(x=1360,y=760)




# Labels
lb_header = tk.Label(window,text= "Julie's Party",font=('Arial',45,"bold"), width= 20,fg="red",bg="lightgrey")
lb_name = tk.Label(label_bg,text= "Customer Name",font=('Arial',14),fg="black",bg="lightgrey")
lb_receipt = tk.Label(label_bg,text= "Receipt Number",font=('Arial',14),fg="black",bg="lightgrey")
lb_item = tk.Label(label_bg,text= "Item Hired",font=('Arial',14),fg="black",bg="lightgrey")
lb_num = tk.Label(label_bg,text= "Quantity of items",font=('Arial',14),fg="black",bg="lightgrey")
# Label positions
lb_header.place(x=0,y=0)
lb_name.place(x=70,y=9)
lb_receipt.place(x=70,y=50)
lb_item.place(x=70,y=100)
lb_num.place(x=70,y=155)


# Create entry boxes
customer_name = tk.Entry(window,width=20, font=('Arial',12))
receipt_num = tk.Entry(window,width=20, font=('Arial',12))
item_hired = tk.Entry(window,width=20, font=('Arial',12))
num_hired = tk.Entry(window,width=20, font=('Arial',12))
del_row = tk.Entry()
# Entry box positions
customer_name.place(x=450,y=200)
receipt_num.place(x=450,y=250)
item_hired.place(x=450,y=300)
num_hired.place(x=450,y=350)
del_row.place





window.mainloop()