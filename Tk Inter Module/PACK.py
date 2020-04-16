from tkinter import *
top=Tk()
frame1=Frame(top)
frame1.pack()

frame2=Frame(top)
frame2.pack(side=BOTTOM)

frame3=Frame(top).pack(side=LEFT)
B1=Button(frame1,text="red",fg="red").pack(side=LEFT)
B2=Button(frame1,text="yellow",fg="yellow").pack(side=LEFT)
B3=Button(frame1,text="blue",fg="blue").pack(side=LEFT)

B4=Button(frame2,text="black",fg="black").pack(side=BOTTOM)

B5=Button(frame3,text="pink",fg="pink").pack(side=LEFT)
