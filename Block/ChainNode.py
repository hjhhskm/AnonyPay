# -*- coding: utf-8 -*-
import hashlib as hasher
import sys
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
        self.account = input["account"]
        self.address = input["address"]
        self.category = input["category"]
        self.amount = input["amount"]
        pass

    def display(self):
        str = '%s : %d\n%s : %s\n%s : %s\n%s : %s\n%s : %f' % ("index", self.index, "account", self.account, \
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

#test
# list = Chain()
# list.append(cNode("a"))
# list.append(cNode("b"))
# for iter in list:
#     print(iter.data)

