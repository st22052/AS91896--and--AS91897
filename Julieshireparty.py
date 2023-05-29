import tkinter as tk
from tkinter import ttk

# Create custom window
window = tk.Tk()
window.title("Julie's hire party")
window.geometry("1100x600") 
window.configure(bg="white")
window.attributes('-fullscreen',True)
# Add shapes
entry_box_bg = tk.Label(window,text= "      ", width=23, height=9,fg="red",bg="#213A5C")
entry_box_bg.place(x=245,y=141)

label_bg = tk.Label(window,text= "      ", width=24, height=9,fg="red",bg="#213A5C")
label_bg.place(x=50,y=141)


# Create custom table
table_frame = tk.Frame()
table_frame.pack(padx=1,pady=1)
table_frame.place(x=1000,y=200)


columns = ("Customer Name", "Receipt Number", "Item Hired", "Number Hired")
treeview = ttk.Treeview(table_frame, columns=columns, show="headings")
treeview.pack(padx=1,pady=1)

entry_frame = ttk.Frame()
entry_frame.pack(padx=1,pady=1)


#Headings for table
for col in columns:
    treeview.heading(col, text=col)


#create function to add data to the table
def add_data():
    Name = customer_name.get()
    Receipt = receipt_num.get()
    Item_Hired = item_hired.get()
    Number_Hired = num_hired.get()
    treeview.insert("", "end", values=(Name, Receipt, Item_Hired, Number_Hired))

# Create buttons to add to table

# submit button
add_button = tk.Button(text="Print Details",font=("Arial",12,"bold"), command=add_data)
add_button.pack(padx=10,pady=300)
add_button.place(x=200,y=100)

btn_append = tk.Button(window,text="Append Details",font=("Arial",12,"bold"))
btn_append.place(x=190,y=300)

# Button to exit application
btn_exit = tk.Button(window,text="Exit application",font=("Arial",13),command=exit)
btn_exit.place(x=1500,y=950)

# Labels
lb_header = tk.Label(window,text= "Julie's Party",font=('Arial',45,"bold"), width= 27,fg="red",bg="lightgrey")
lb_name = tk.Label(window,text= "Customer Name",font=('Arial',11),fg="black",bg="lightgrey")
lb_receipt = tk.Label(window,text= "Receipt Number",font=('Arial',11),fg="black",bg="lightgrey")
lb_item = tk.Label(window,text= "Item Hired",font=('Arial',11),fg="black",bg="lightgrey")
lb_num = tk.Label(window,text= "Number Hired",font=('Arial',11),fg="black",bg="lightgrey")
# Label positions
lb_header.place(x=0,y=0)
lb_name.place(x=80,y=147)
lb_receipt.place(x=81,y=176)
lb_item.place(x=101,y=210)
lb_num.place(x=90,y=240)


# Create entry boxes
customer_name = tk.Entry(window,width=25)
receipt_num = tk.Entry(window,width=25)
item_hired = tk.Entry(window,width=25)
num_hired = tk.Entry(window,width=25)
del_row = tk.Entry()
# Entry box positions
customer_name.place(x=250,y=150)
receipt_num.place(x=250,y=180)
item_hired.place(x=250,y=210)
num_hired.place(x=250,y=240)
del_row.place





window.mainloop()