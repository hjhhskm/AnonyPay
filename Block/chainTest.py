from ChainJson import *
from ChainNode import *
from ChainRedis import *
import Server.transAction
#test function
testIndex = 1
list = {}
list['index'] = 1
list['time'] = "14:04"
list['pre_hash'] = "0"
list['listNum'] = 1
list['node'] = {'index' : 0, 'tfrom' : '0_0_0','account' : '12312312','address' : '0','category' : 'send','amount' : 100}
info2 = {'index': 1, 'tfrom' : 'asdad','account': '0_0_0', 'address': 'a3ab1f5779f491879198ea5a450cf32be59e19fa', 'category': 'recv', 'amount': 100}
testIndex2 = 2
list2 = {}
list2['index'] = 1
list2['time'] = "14:04"
list2['pre_hash'] = "0"
list2['listNum'] = 1
info3 = {'index' : 0, 'tfrom' : '0_0_0','account' : '12312312','address' : '0','category' : 'send','amount' : 100}
info4 = {'index': 1, 'tfrom' : 'asdad','account': '0_0_0', 'address': 'ba33bf5d1e25375a233eda1b1139d4f2c20c07c1', 'category': 'recv', 'amount': 50}


node = ChainNodeList(**list)
node.appendNode(Node(**list['node']))
node.appendNode(Node(**info2))
line = Chain()
line.append(cNode(node))
newNode = None

node2 = ChainNodeList(**list2)
node2.appendNode(Node(**info3))
node2.appendNode(Node(**info4))

line2 = Chain()
line2.append(cNode(node2))
#back
backUpToJson(line,testIndex)
backUpToJson(line2,testIndex2)
inNode = recoverFromFile(testIndex)

b_chain = Chain()
b_chain.append(cNode(inNode))
b_chain.append(cNode(node2))
add_list = ['ba33bf5d1e25375a233eda1b1139d4f2c20c07c1','a3ab1f5779f491879198ea5a450cf32be59e19fa']
print(Server.transAction.calcOverage(Server.transAction.calcUtxo(add_list,b_chain)))
# rds = startConnectedToRedis()
#
# setChainNode(inNode,rds)
# getChainNode(1,rds).display()
#recoverFromFile(newNode,testIndex)