from tkinter import *
import BackEnd

def view_command():
    list1.delete(0, END)
    for row in BackEnd.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in BackEnd.search(name.get(), movie_title.get(), time.get(), phone_no.get(), address.get()):
        list1.insert(END, row)

def insert_command():
    BackEnd.insert(name.get(), movie_title.get(), time.get(), phone_no.get(), address.get())
    list1.delete(0, END)
    list1.insert(END, (name.get(), movie_title.get(), time.get(), phone_no.get(), address.get()))

def get_selected_row(event):
    global  selected_tuple
    index=list1.curselection()
    selected_tuple=list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])


def delete_command_selected():
    BackEnd.delete(selected_tuple[0])

def update_command_selected():

    BackEnd.update(selected_tuple[0], name.get(), movie_title.get(), time.get(), phone_no.get(), address.get())

def rent_command():
    amount = BackEnd.calculate(cost.get(), time.get())
    list2.delete(0, END)
    list2.insert(END, "The Total Amount to be Paid:")
    list2.insert(END, amount)


window = Tk()


l1 = Label(window, text="Name of the Person")
l1.grid(row=0, column=0)

l2 = Label(window, text="Movie Title")
l2.grid(row=1, column=0)

l3 = Label(window, text="Time")
l3.grid(row=2, column=0)

l4 = Label(window, text="Phone Number")
l4.grid(row=3, column=0)

l5 = Label(window, text="Address")
l5.grid(row=4, column=0)


name = StringVar()
e1 = Entry(window, textvariable=name)
e1.grid(row=0, column=1)

movie_title = StringVar()
e2 = Entry(window, textvariable=movie_title)
e2.grid(row=1, column=1)

time = StringVar()
e3 = Entry(window, textvariable=time)
e3.grid(row=2, column=1)

phone_no = StringVar()
e4 = Entry(window, textvariable=phone_no)
e4.grid(row=3, column=1)

address = StringVar()
e5 = Entry(window, textvariable=address)
e5.grid(row=4, column=1)

b1 = Button(window, text="Add Entry", width=12, command=insert_command)
b1.grid(row=6, column=0)

b4 = Button(window, text="Search Entry", width=12, command=search_command)
b4.grid(row=7, column=0)

b5 = Button(window, text="View All", width=12, command=view_command)
b5.grid(row=8, column=0)

b5 = Button(window, text="Calculate Rent", width=12, command=rent_command)
b5.grid(row=8, column=1)

list1 = Listbox(window, width=40, height=10)
list1.grid(row=9, column=0, rowspan=5, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=9, column=2, rowspan=5)

sb2 = Scrollbar(window, orient=HORIZONTAL)
sb2.grid(row=14,column=0, columnspan=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

b6 = Button(window, text="Delete Selected", command=delete_command_selected)
b6.grid(row=15, column=0)

b7 = Button(window, text="Update Selected", command=update_command_selected)
b7.grid(row=15, column=1)

l6 = Label(window, text="Cost of the Movie")
l6.grid(row=16, column=0)

cost = StringVar()
e6 = Entry(window, textvariable=cost)
e6.grid(row=16, column=1)

list2 = Listbox(window, width=40, height=3)
list2.grid(row=17, column=0, columnspan=2)

window.mainloop()
