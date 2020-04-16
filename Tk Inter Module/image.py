import PIL
import os
import tkinter
root=tkinter.Tk()
img=ImageTk.PhotoImage(Image.open('harnath.png'))
panel=tk.Lable(image=img)
panal.pack()
root.mainloop()
