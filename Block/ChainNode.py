# -*- coding: utf-8 -*-
import hashlib as hasher
import sys
import os
import datetime as dater

class cNode:
    def __init__(self,nodeList = None,node_next = None):
        self.data = nodeList
        self._next = node_next

class Chain:
    def __init__(self):
        self.nums = 0
        self.nowNode = None
        self.head = cNode()
        self.tail = self.head
        pass

    def append(self,nodeList):
        self.nums += 1
        self.tail._next = nodeList
        self.tail = nodeList
        pass

    def __iter__(self):
        self.nowNode = self.head
        return self
    def __next__(self):
        self.nowNode = self.nowNode._next
        if self.nowNode == None:
            raise  StopIteration
        return self.nowNode

class Node:
    def __init__(self,**input):
        self.index = input['index']
        self.tfrom = input['tfrom']
        self.account = input["account"]
        self.address = input["address"]
        self.category = input["category"]
        self.amount = input["amount"]
        pass

    def display(self):
        str = '%s : %d\n%s : %s\n%s : %s\n%s : %s\n%s : %s\n%s : %f' % ("index", self.index,"from",self.tfrom, "account", self.account, \
               "address", self.address, "category", self.category,"amount", self.amount)
        return str

class ChainNodeList:
    def __init__(self,**input):
        self.index = input["index"]
        self.time = input["time"]
        self.pre_hash = input["pre_hash"]
        try:
            self.listNum = input['nums']
        except KeyError:
            self.listNum = 0
        if "hash" in input:
            self.hash = input['hash']
        else:
            self.hash = self.hash_block()
        self.point = Chain()
        pass

    def hash_block(self):
        sha = hasher.sha256()
        text = str(self.index) + str(self.time) + str(self.pre_hash)
        sha.update(str(text).encode("utf-8"))
        return sha.hexdigest()

    def appendNode(self,nextNode):
        if isinstance(nextNode,Node):
            self.point.append(cNode(nextNode))
            self.listNum += 1
            return 0
        else:
            print("[ChainNode]:you can't append AnonyPay node which is not type of Node\nerror type append")
            return 1
        pass

    def display(self):
        str = '%s : %d\n%s : %s\n%s : %s\n%s : %s\n%s : %s' % ("index", self.index, \
               "create time ", self.time, "previous hash", self.pre_hash, "deal nums", self.listNum, "node hash", self.hash)
        print("++++++++++++Chain Info:+++++++++++++")
        print(str)
        for disNode in self.point:
            print("----------Transaction Info----------")
            if disNode.data.index == -1:
                continue
            print(disNode.data.display())

def createNewBlock(pub_list,pay_list,cash_list,all_amount,cashNum,change_addr,pay_addr):
    block = {}
    block['index'] = len(os.listdir("../data/Chain"))
    block['time'] = dater.datetime.now().strftime('%Y%m%d%H%M%S%f')
    listNum = len(pub_list)

    with open("../data/Chain/ChainNode_"+str(block['index'])+".json","r") as f:
        #warning :直接读取文件第6行获取pre_hash值，如果文件结构发生变动，此处需要修改
        for i in range(5):
            f.readline()
        block['pre_hash'] = f.readline().split('\"')[3]
        f.close()
    #需要加上recv交易
    create_block = ChainNodeList(**block)

    #找零
    trans_info = {}
    trans_info['index'] = 0
    trans_info['tfrom'] = "0"
    trans_info['account'] = str(pub_list[0])
    trans_info['address'] = pay_addr
    trans_info['category'] = 'send'
    trans_info['amount'] = int(cashNum)
    pay_list[0] -= int(cashNum)
    create_block.appendNode(Node(**trans_info))

    #send
    for iter in range(0,listNum):
        trans_info = {}
        trans_info['index'] = iter+1
        trans_info['tfrom'] = "0"
        trans_info['account'] = pub_list[iter]
        trans_info['address'] = pay_addr
        trans_info['category'] = 'send'
        trans_info['amount'] = pay_list[iter]
        create_block.appendNode(Node(**trans_info))

    trans_info = {}
    trans_info['index'] = listNum+1
    trans_info['tfrom'] = "0"
    trans_info['account'] = "0"
    trans_info['address'] = pay_addr
    trans_info['category'] = 'recv'
    trans_info['amount'] = int(all_amount)
    create_block.appendNode(Node(**trans_info))

    trans_info = {}
    trans_info['index'] = listNum + 2
    trans_info['tfrom'] = "0"
    trans_info['account'] = "0"
    trans_info['address'] = change_addr
    trans_info['category'] = 'recv'
    trans_info['amount'] = int(cashNum)
    create_block.appendNode(Node(**trans_info))

    create_block.display()
    pass
#test
# list = Chain()
# list.append(cNode("a"))
# list.append(cNode("b"))
# for iter in list:
#     print(iter.data)

