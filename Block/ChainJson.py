import json
from Block import ChainNode
import simplejson

def recoverFromFile(chainIndex):
    if chainIndex == -1:
        print("file name is none")
        return -1

    dir = "../data/Chain/ChainNode_" + str(chainIndex) + ".json"
    file = open(dir,"r")
    if file == None:
        print("no such file or directory")
        return -1
    lines = file.readlines()
    nowdata = ""
    for line in lines:
        nowdata = nowdata + line
    get_json = simplejson.loads(nowdata)
    file.close()

    chainNode = ChainNode.ChainNodeList(**get_json)
    for get_node in get_json['point']:
        chainNode.appendNode(ChainNode.Node(**get_node))
    return chainNode
    pass

def backUpToJson(chainLine,chainIndex):
    if chainLine == None:
        print("block chain is none")
        return -1
    if chainIndex == -1:
        print("file name is none")
        return -1

    dir = "../data/Chain/ChainNode_" + str(chainIndex) + ".json"
    file = open(dir,"w")
    if file == None:
        print("system err")
        return 1
#两层for将区块和交易内容存入文件
    for line in chainLine :
        node_str = []
        for node in line.data.point:
            node_str.append({"index" : node.data.index,"tfrom" : node.data.tfrom, "account" : node.data.account, "address" : node.data.address,\
                       "category" : node.data.category,"amount" : node.data.amount})
        block_str = {'index' : line.data.index,'time': line.data.time, 'pre_hash':\
                    line.data.pre_hash, 'listNum': line.data.listNum, 'hash': line.data.hash,'point' : node_str}
        json_str = json.dumps(block_str, indent=4)
        file.write(json_str)
    file.close()

# #test function
# testIndex = 1
# list = {}
# list['index'] = 1
# list['time'] = "14:04"
# list['pre_hash'] = "0"
# list['listNum'] = 1
# list['node'] = {'index' : 0, 'account' : '12312312','address' : 'ba33bf5d1e25375a233eda1b1139d4f2c20c07c1','category' : 'send','amount' : 100}
# node2 = {'index': 1, 'account': '2324325', 'address': 'ad3e021ac0be4ed71fe2ebd70d242bf00ca97476', 'category': 'recv', 'amount': 100}
# node = ChainNodeList(**list)
# node.appendNode(Node(**list['node']))
# node.appendNode(Node(**node2))
# line = Chain()
# line.append(cNode(node))
# newNode = None
# #back
# backUpToJson(line,testIndex)
# recoverFromFile(testIndex).display()
# #recoverFromFile(newNode,testIndex)