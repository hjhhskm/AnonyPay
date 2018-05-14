from PIL import *
from tkinter import *

def show(event):
    img = open("../image/pj.png")
    img = PhotoImage(img)
    can.insert(img)

root=Tk()
root.title('Canvas')
can=Canvas(root,bg='white')
can.grid()
button=Button(height=1,width=20,text='button',bg='red')
button.bind("<Button-1>",show)
button.grid()

img = open("../image/pj.png")
img = PhotoImage(img)

root.mainloop()