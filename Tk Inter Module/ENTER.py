from tkinter import *

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master,text="-------WELCOME TO OUR BANK-------- ").grid(row=0)
Lable(master,text="----all your life is safe hers-----").grid(row=1)
Label(master, text="Account number:").grid(row=2)
Label(master, text="pin:").grid(row=3)

e1 = Entry(master).grid(row=0, column=1)
e2 = Entry(master)

grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
