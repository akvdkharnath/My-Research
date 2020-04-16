from tkinter import *
top=Tk()
def bc():
    
Button(top,text="c",width=4,height=2,command=bc).grid(row=0,column=1)
Button(top,text="+/-",width=4,height=2,command=np).grid(row=0,column=2)
Button(top,text="%",width=4,height=2,command=pp).grid(row=0,column=3)
Button(top,text="DEL",width=4,height=2,command=DEL).grid(row=0,column=4)

Button(top,text="7",width=4,height=2,command=NUM7).grid(row=1,column=1)
Button(top,text="8",width=4,height=2,command=NUM8).grid(row=1,column=2)
Button(top,text="9",width=4,height=2,command=NUM9).grid(row=1,column=3)
Button(top,text="DIV",width=4,height=2,command=DIV).grid(row=1,column=4)

Button(top,text="4",width=4,height=2,command=NUM4).grid(row=2,column=1)
Button(top,text="5",width=4,height=2,command=NUM5).grid(row=2,column=2)
Button(top,text="6",width=4,height=2,command=NUM6).grid(row=2,column=3)
Button(top,text="MUL",width=4,height=2,command=MUL).grid(row=2,column=4)

Button(top,text="1",width=4,height=2,command=NUM1).grid(row=3,column=1)
Button(top,text="2",width=4,height=2,command=NUM2).grid(row=3,column=2)
Button(top,text="3",width=4,height=2,command=NUM3).grid(row=3,column=3)
Button(top,text="SUB",width=4,height=2,command=SUB).grid(row=3,column=4)

Button(top,text="0",width=4,height=2,command=NUM0).grid(row=4,column=1)
Button(top,text=".",width=4,height=2,command=DOT).grid(row=4,column=2)
Button(top,text="=",width=4,height=2,command=EQUAL).grid(row=4,column=3)
Button(top,text="ADD",width=4,height=2,command=ADD).grid(row=4,column=4)

