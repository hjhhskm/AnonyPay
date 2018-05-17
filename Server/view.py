#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk
import cryptor
import Block.ChainNode as chainNode
import Block.ChainJson as chainJson
import transAction
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
        err_info = Label(acc_top,text="\t\t\t已存在该密钥名称，请更换\t\t\t\t").pack()
    else:
        user_name = Label(acc_top,text="创建成功，密钥名称为"+e_user.get()).pack()
        user_value = Label(acc_top, text="钱包地址为："+cryptor.getPayAddr(e_user.get())).pack()
    # lb.insert(END,getRandom())

#transaction function
def transAuto():
    trans_cash = int(e_trans.get())
    trans_addr = e_addr.get()

    utxo_list = transAction.calcUtxo(cryptor.getWalletAddListByName(list_item), e_Chain)
    overage = transAction.calcOverage(utxo_list)
    try:
        if trans_cash > overage:
            acc_top = Toplevel()
            err_info = Label(acc_top, text="\t\t\t余额不足，请充值后重试\t\t\t\t").pack()
            return
    except ValueError:
        return
    ave_list = {}
    item_nums = 0
    for u_key in utxo_list:
        ave_list[list_item[item_nums]] = 0

        for u_node in utxo_list[u_key]:
            ave_list[list_item[item_nums]] += utxo_list[u_key][u_node]
        item_nums += 1

    sort_list = sorted(ave_list.items(), key=lambda x:x[1],reverse=True)
    #algorithm
    num_choice = -1
    choice_list = []
    pay_list = []
    count = 0
    pay_Choice = 0
    for node in sort_list:
        if node[1] >= trans_cash:
            num_choice = node[0]
            pay_Choice = node[1]
        else:
            break
    #整个钱包组每个钱包都没有支付额大

    if num_choice == -1:
        count = trans_cash
        for node in sort_list:
            choice_list.append(node[0])
            pay_list.append(node[1])
            count -= node[1]
            if count <= 0:
                break
    #存在单个比支付额大的钱包
    else:
        choice_list.append(num_choice)
        pay_list.append(pay_Choice)
        count = trans_cash - pay_Choice
    ret = transAction.calcPayAccount(choice_list,pay_list,trans_cash,0-count,trans_addr)
    #如果交易成功，则打印相关信息
    if ret == 0:
        acc_top = Toplevel()
        err_info = Label(acc_top, text="\t\t\t交易成功\t\t\t\t").pack()
    #更新余额
    getOverage()
    pass

#Overage calculation
def getOverage():
    overage = transAction.calcOverage(transAction.calcUtxo(cryptor.getWalletAddListByName(list_item),e_Chain))
    p_overage = Label(root,text=str(overage)).pack(pady=10)
    pass

#struct define
e_Chain = chainNode.Chain()
for i in range(0,len(os.listdir("../data/Chain"))):
    e_Chain.append(chainNode.cNode(chainJson.recoverFromFile(i+1)))

# for node in e_Chain:
#     print(node.data.index)

#start window and entry
root = Tk()
root.wm_title("Anony Pay")
root.geometry("400x300+300+100")
var = StringVar()
e_user = Entry(root)
e_trans = Entry(root)
e_addr = Entry(root)
p_overage = Label(root)
#ListBox setting
lb = Listbox(root,listvariable = var)
list_item = getWalletList()
if list_item != -1:
    for item in list_item:
        lb.insert(END,item)
scroll = Scrollbar(root)
lb.configure(yscrollcommand = scroll.set)
lb.pack(side=LEFT, fill=BOTH,padx=10,pady=10,ipadx=5)
scroll.pack(side=LEFT)
scroll['command'] = lb.yview
lb.bind('<ButtonRelease-1>', printQRCode)
lb.pack()

#pack the entries and buttons
e_user.pack(pady=10,padx=10)
Button(root,text="新建钱包",command=createAccountInfo).pack(padx=10)
Label(text="交易金额").pack()
e_trans.pack(padx=10,pady=10)
Label(text="交易地址").pack()
e_addr.pack(padx=10,pady=10)
Button(root,text="执行交易",command=transAuto).pack(padx=10)
Button(root,text="查询余额",command=getOverage).pack(padx=10)
getOverage()
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

