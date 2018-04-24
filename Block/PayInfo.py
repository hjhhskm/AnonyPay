# -*- coding: utf-8 -*-

import datetime as dater

global list_num

def InitListNum(list_num_history):
    global list_num

    list_num = list_num_history
    pass
def InitListNum():
    global list_num

    list_num = 0
    pass

class Paylist:

    def __init__(self,list_vendor,list_customer,list_amount):
        global list_num

        InitListNum()
        self.num = list_num
        self.timestamp = dater.datetime.now()
        self.vendor = list_vendor
        self.customer = list_customer
        self.amount = list_amount
        pass

    def print_list(self):
        list_str = '%s\t: \t%d\n%s\t:\t%s\n%s\t:\t%s\n%s\t:\t%s\n%s\t:\t%d\n' % \
                   ("number" , self.num , "time" , str(self.timestamp) ,"vendor" , self.vendor , \
                    "payer" , self.customer ,"amount" , self.amount)
        return  list_str

# first_list = Paylist("zhang3","li4",100)
# print(first_list.print_list())