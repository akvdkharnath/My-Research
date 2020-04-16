cls
import tkinter
top=tkinter.Tk()
def Yes():
    print('hai harnath how r u')
    yes=tkinter.Tk()
    y1=tkinter.Label(yes,text="hai harnath how r u",)
    y1.pack()    
def No():
    print('then who r u')
    
L1=tkinter.Label(top,text="my name is harnath",bg="blue",fg="yellow",bd=5,height=5,underline=10,)
B1=tkinter.Button(top,text="yes",fg="blue",command=Yes,activebackground="yellow")
B2=tkinter.Button(top,text="no",fg="red",command=No,activebackground="yellow")
top.title("name program")  
top.geometry("500x500")
L1.pack()
B1.pack(side=tkinter.LEFT)
B2.pack(side=tkinter.RIGHT)

# bg=background colour   bd  =broder size      activebackground=colour change when mouse is on it
# fg=text colour         command=instruction    
  
