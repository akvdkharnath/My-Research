from tkinter import *
from tkinter import messagebox
main=Tk()
main.geometry("250x250")
def hello(event):
    msg=messagebox.showinfo("hello pyt","message from m1")
def hello2(event):
    second=Tk()
    Label(second,text="center button").place(x=50,y=50)
def hello3(event):
    second=Tk()
    Label(second,text="double click").pack()
def hello4(event):
    second=Tk()
    Label(second,text="emter in to box").pack()
b1=Button(main,text="first")
b2=Button(main,text="second")
b1.bind('<Button-1>',hello)
b1.bind('<Button-2>',hello2)
b1.bind('<Double-Button-1>',hello3)
b1.bind('<Enter>',hello4)
b1.place(x=20,y=40)
