from tkinter import *
top=Tk()
def red():
    ans=Tk()
    Label(ans,text="red").pack()
def yellow():
    ans=Tk()
    Label(ans,text="yellow").place(x=50,y=50)
def blue():
    ans=Tk()
    Label(ans,text="blue").place(x=50,y=150)
def black():
    ans=Tk()
    Label(ans,text="black").place(x=50,y=200)
def pink():
    ans=Tk()
    Label(ans,text="pink").place(x=50,y=250)
B1=Button(top,text="red",fg="red",command=red).place(x=10,y=10)
B2=Button(top,text="yellow",fg="yellow",command=yellow).place(x=10,y=50)
B3=Button(top,text="blue",fg="blue",command=blue).place(x=10,y=150)
B4=Button(top,text="black",fg="black",command=black).place(x=10,y=200)
B5=Button(top,text="pink",fg="pink",command=pink).place(x=10,y=250)
top.geometry("300x300+100+100")
