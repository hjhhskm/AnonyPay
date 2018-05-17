import Server.cryptor
import rsa

def checkTransInfo(publicKey,sign,amount,addr,t_addr):
    message = str(amount)+addr
    return Server.cryptor.verifyByPub(publicKey,message,sign) and (Server.cryptor.makePayAddr(publicKey) == t_addr)

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


pub = Server.cryptor.getPub("hanjh")
p_add = Server.cryptor.makePayAddr(pub)
signa = Server.cryptor.signByPriv("hanjh","100ad3e021ac0be4ed71fe2ebd70d242bf00ca97476")
print(str(checkTransInfo(pub,signa,100,"ad3e021ac0be4ed71fe2ebd70d242bf00ca97476",p_add)))