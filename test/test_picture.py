from PIL import *
from tkinter import *


root=Tk()
root.title('Canvas')
can=Canvas(root,bg='white')
can.grid()
button=Button(height=1,width=20,text='button',bg='red')
button.bind("<Button-1>",show)
button.grid()

root.mainloop()