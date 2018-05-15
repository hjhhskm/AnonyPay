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
    chooseName = lb.get(lb.curselection())
    top = Toplevel()
    qrLoad = Image.open('../image/'+chooseName+'.png')
    render = ImageTk.PhotoImage(qrLoad)
    imgLoad = Label(top,image=render)
    imgLoad.image = render
    imgLoad.pack()
    Label(top,text=cryptor.getPayAddr(chooseName)).pack()

def getRandom():
    return os.urandom(10)

def getWalletList():
    if os.path.isdir("../KeyFile"):
        return os.listdir("../KeyFile")
    else:
        return -1


def createKey():
    if cryptor.createKey(e_user.get()) == -1:
        return -1
    lb.insert(END,e_user.get())
    list_item.append(e_user.get())
    return 0

def createAccountInfo():
    acc_top = Toplevel()
    if createKey() == -1:
        err_info = Label(acc_top,text="已存在该密钥名称，请更换").pack()
    else:
        user_name = Label(acc_top,text="创建成功，密钥名称为"+e_user.get()).pack()
        user_value = Label(acc_top, text="钱包地址为："+cryptor.getPayAddr(e_user.get())).pack()
    # lb.insert(END,getRandom())

#start
root = Tk()
root.wm_title("Anony Pay")
root.geometry("400x300+300+100")
var = StringVar()
e_user = Entry(root)

lb = Listbox(root,listvariable = var)
list_item = getWalletList()
if list_item != -1:
    for item in list_item:
        lb.insert(END,item)
scroll = Scrollbar(root)
scroll.pack()
lb.configure(yscrollcommand = scroll.set)
lb.pack(side=LEFT, fill=BOTH)
scroll['command'] = lb.yview
lb.bind('<ButtonRelease-1>', printQRCode)
lb.pack()

e_user.pack()
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

