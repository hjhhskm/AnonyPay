from ChainJson import *
from ChainNode import *
from ChainRedis import *

#test function
testIndex = 1
list = {}
list['index'] = 1
list['time'] = "14:04"
list['pre_hash'] = "0"
list['listNum'] = 1
list['node'] = {'index' : 0, 'account' : '12312312','address' : 'ba33bf5d1e25375a233eda1b1139d4f2c20c07c1','category' : 'send','amount' : 100}
node2 = {'index': 1, 'account': '2324325', 'address': 'ad3e021ac0be4ed71fe2ebd70d242bf00ca97476', 'category': 'recv', 'amount': 100}
node = ChainNodeList(**list)
node.appendNode(Node(**list['node']))
node.appendNode(Node(**node2))
line = Chain()
line.append(cNode(node))
newNode = None
#back
backUpToJson(line,testIndex)
inNode = recoverFromFile(testIndex)


rds = startConnectedToRedis()

setChainNode(inNode,rds)
getChainNode(1,rds).display()
#recoverFromFile(newNode,testIndex)