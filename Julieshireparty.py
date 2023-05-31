import tkinter as tk
from tkinter import ttk
from tkinter import *
# Create custom window
window = tk.Tk()
window.title("Julie's hire party")
window.geometry("1100x600") 
window.configure(bg="white")
window.attributes('-fullscreen',True)
# Add shapes
entry_box_bg = tk.Label(window, width=30, height=17,fg="red",bg="#213A5C")
entry_box_bg.place(x=433,y=190)

label_bg = tk.Label(window, width=30, height=17,fg="red",bg="#213A5C")
label_bg.place(x=200,y=190)

button_bg = tk.Label(window, width=64, height=10, bg="#213A5C")
button_bg.place(x=200,y=465)


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


#Headings for table
for col in columns:
    treeview.heading(col, text=col)


#create function to add data to the table
def add_data():
    Name = customer_name.get()
    try:
        Receipt = int(receipt_num.get())
    except ValueError:
        error.config(text="Please enter a number")


    Item_Hired = item_hired.get()
    Number_Hired = num_hired.get()
    treeview.insert("", "end", values=(Name, Receipt, Item_Hired, Number_Hired))

error = Label(window, text='', bg="yellow")
error.place(x=450,y=270)

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
del_btn = ttk.Button(window, text="Delete selected row", width=23, command=delete)
del_btn.place(x=960,y=760)
delete_all = ttk.Button(window, text="Delete all", width=23, command=delete_all)
delete_all.place(x=1100,y=760)


# Create buttons to add to table

# submit button
add_button = tk.Button(text="Print Details",font=("Arial",12,"bold"), command=add_data)
add_button.pack(padx=10,pady=300)
add_button.place(x=535,y=480)

btn_append = tk.Button(window,text="Append Details",font=("Arial",12,"bold"))
btn_append.place(x=400,y=480)

# Button to exit application
btn_exit = tk.Button(window,text="Exit application",font=("Arial",13),command=exit)
btn_exit.place(x=1360,y=760)




# Labels
lb_header = tk.Label(window,text= "Julie's Party",font=('Arial',45,"bold"), width= 23,fg="red",bg="lightgrey")
lb_name = tk.Label(window,text= "Customer Name",font=('Arial',14),fg="black",bg="lightgrey")
lb_receipt = tk.Label(window,text= "Receipt Number",font=('Arial',14),fg="black",bg="lightgrey")
lb_item = tk.Label(window,text= "Item Hired",font=('Arial',14),fg="black",bg="lightgrey")
lb_num = tk.Label(window,text= "How many items hired",font=('Arial',14),fg="black",bg="lightgrey")
# Label positions
lb_header.place(x=0,y=0)
lb_name.place(x=240,y=200)
lb_receipt.place(x=240,y=250)
lb_item.place(x=240,y=300)
lb_num.place(x=225,y=350)


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