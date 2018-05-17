import Server.cryptor as Cryptor
import rsa
import Block.ChainNode as chainNode

def checkTransInfo(publicKey,sign,amount,addr,t_addr):
    message = str(amount)+addr
    return Cryptor.verifyByPub(publicKey,message,sign) and (Cryptor.makePayAddr(publicKey) == t_addr)

#计算utxo：
#遍历本地地址表，根据支付一定后于收入发生，每次都对node进行判断，将recv（收入）对应的区块好+记录号节点对应的金额
# 全部记录在utxo列表，即为未使用，将send（支付）对应的区块好+记录号节点对应的金额置空，即为已使用。遍历结束所得到的
# 集合即为所有地址对应的utxo集。通过该集合可计算余额
def calcUtxo(CountList,chainList):
    utxo_list = {}
    nums = 0
    for count in CountList:
        utxo_list[count] = {}
        for chain in chainList:
            for node in chain.data.point:
                if node.data.category == "recv":
                    if node.data.address == count:
                        utxo_list[count][str(chain.data.index)+"_"+str(node.data.index)] = node.data.amount
                elif node.data.category == "send":
                    if node.data.tfrom.split("_")[2] == count:
                        utxo_list[count][str(chain.data.index) + "_" + str(node.data.index)] = None

    return utxo_list

def calcOverage(utxo_list):
    r_amount = 0
    for c_key in utxo_list:
        for c_index in utxo_list[c_key]:
            if utxo_list[c_key][c_index] != None:
                r_amount += utxo_list[c_key][c_index]

    return r_amount

def calcPayAccount(name_list,pay_list,amount,cash,pay_addr):
    #验证支付签名
    sign_list = []
    pub_list = []
    addr_list = []
    for name in name_list:
        pub_list.append(Cryptor.getPub(name))
        addr_list.append(Cryptor.getPayAddr(name))
        sign_list.append(Cryptor.signByPriv(name,str(amount)+pay_addr))
    iter = 0
    for name in name_list:
        res = checkTransInfo(pub_list[iter],sign_list[iter],amount,pay_addr,addr_list[iter])
        if res != True:
            return -1
    #地址列表最后一个地址为找零地址（暂定)
    print(str(addr_list[len(addr_list)-1]))
    return chainNode.createNewBlock(pub_list,pay_list,addr_list,amount,cash,addr_list[len(addr_list)-1],pay_addr)
    pass

pub = Cryptor.getPub("hanjh")
p_add = Cryptor.makePayAddr(pub)
signa = Cryptor.signByPriv("hanjh","100ad3e021ac0be4ed71fe2ebd70d242bf00ca97476")
print(str(checkTransInfo(pub,signa,100,"ad3e021ac0be4ed71fe2ebd70d242bf00ca97476",p_add)))