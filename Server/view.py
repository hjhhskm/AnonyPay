#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk
import cryptor
import os

def printItem(event):
    tkinter.messagebox.showinfo("地址",str(lb.get(lb.curselection())))
    print(lb.get(lb.curselection()))

def printQRCode(event):
    top = Toplevel()
    qrLoad = Image.open('../image/pj.png')
    render = ImageTk.PhotoImage(qrLoad)
    imgLoad = Label(top,image=render)
    imgLoad.image = render
    imgLoad.pack()
    Label(top,text=lb.get(lb.curselection())).pack()

def getRandom():
    return os.urandom(10)

def createKey():
    cryptor.createKey(e_user.get())
    lb.insert(END,e_user.get())

def createAccountInfo():
    top = Toplevel()
    e_user = Entry(top)
    l_user = Label(top, text='名称：').pack()
    e_user.bind("<Return>",createKey)
    e_user.pack()
    Button(top, text="生成", command=createKey).pack()
    # lb.insert(END,getRandom())

root = Tk()
root.wm_title("Anony Pay")
root.geometry("400x300+300+100")

#top define

e_user = Entry()

var = StringVar()

lb = Listbox(root,listvariable = var)
list_item = [1,2,3,4]
for item in list_item:
    lb.insert(END,item)

scroll = Scrollbar(root)
scroll.pack()
lb.configure(yscrollcommand = scroll.set)
lb.pack(side=LEFT, fill=BOTH)
scroll['command'] = lb.yview

lb.bind('<ButtonRelease-1>', printQRCode)
lb.pack()

Button(root,text="新建钱包",command=createAccountInfo).pack()
# menubar = Menu(root)
# menulist1 = Menu(root)
#
# for item in ["新建","打开","保存","另存为"]:
#     menulist1.add_command(label = item)
#
# menubar.add_cascade(label = "文件",menu = menulist1)
#
# root['menu'] = menubar

root.mainloop()