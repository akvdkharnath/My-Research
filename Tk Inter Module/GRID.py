from tkinter import *
top=Tk()
b=0
for r in range(6):
    for c in range(6):
        b=b+1
        Button(top,text=str(b)).grid(row=r,column=c)
