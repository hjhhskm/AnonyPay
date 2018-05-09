import redis

import Block.ChainNode
#与redis操作的相关函数

# 与redis建立连接
def startConnectedToRedis(nums = 0):
    redis_connect = redis.Redis(host="123.206.190.67",port=6379,db=nums)
    return redis_connect

#关闭指定的redis连接
def closeConnectedRedis(redis_connect):
    if(redis_connect != None):
        redis_connect.close()
        print("close connected success")
    else:
        print("connected is none")
    pass

#通过name查找Block编号
def getBlockIndexByName(chainName, redis_connect):
    if(redis_connect == None):
        print("connect is None,please check")
        pass
    if chainName == None:
        print("no such chainName")
        return -1
    else:
        chainIndex = redis_connect.get(chainName)
        if chainIndex == None:
            print("no such chainName")
            return -1
        else:
            return chainIndex

#通过index查询时间
def getBlockTimeById(chain_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if(chain_index == -1):
        print("the index is not exist")
        pass
    else:
        blockTime = redis_connect.get(chain_index+"time")
        if blockTime == None:
            print("can't find the time")
            return -1
        return blockTime

#通过index查询上一链的hash
def getBlockPreHashById(chain_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if(chain_index == -1):
        print("the index is not exist")
        pass
    else:
        blockPreHash= redis_connect.get(chain_index+"pre")
        if blockPreHash == None:
            print("can't find the previous block hash")
            return -1
        return blockPreHash

#通过index查询本链hash
def getBlockHashById(chain_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if(chain_index == -1):
        print("the index is not exist")
        pass
    else:
        blockHash= redis_connect.get(chain_index+"hash")
        if blockHash == None:
            print("can't find the now block hash")
            return -1
        return blockHash

#通过index查询交易数
def getBlockListNumshById(chain_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if(chain_index == -1):
        print("the index is not exist")
        pass
    else:
        listNums= redis_connect.get(chain_index+"nums")
        if listNums == None:
            print("can't find the list numbers")
            return -1
        return listNums

#通过链index和交易index查询交易账户
def getListAccountById(chain_index, list_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if (chain_index == -1):
        print("the chain index is not exist")
        pass
    if(list_index == -1):
        print("the list index is not exist")
        pass
    else:
        listNums= redis_connect.get(chain_index+"li"+list_index+"act")
        if listNums == None:
            print("can't find the list numbers")
            return -1
        return listNums

#通过链index和交易index查询交易地址
def getListAccountById(chain_index, list_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if (chain_index == -1):
        print("the chain index is not exist")
        pass
    if(list_index == -1):
        print("the list index is not exist")
        pass
    else:
        listAddr= redis_connect.get(chain_index+"li"+list_index+"add")
        if listAddr == None:
            print("can't find the transaction address")
            return -1
        return listAddr

#通过链index和交易index查询操作类型
def getListCategoryById(chain_index, list_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if (chain_index == -1):
        print("the chain index is not exist")
        pass
    if(list_index == -1):
        print("the list index is not exist")
        pass
    else:
        listCate= redis_connect.get(chain_index+"li"+list_index+"cate")
        if listCate == None:
            print("can't find the Category")
            return -1
        return listCate

#通过链index和交易index查询交易金额
def getListAmountById(chain_index, list_index, redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if (chain_index == -1):
        print("the chain index is not exist")
        pass
    if(list_index == -1):
        print("the list index is not exist")
        pass
    else:
        listAmount= redis_connect.get(chain_index+"li"+list_index+"amt")
        if listAmount == None:
            print("can't find the Amount")
            return -1
        return listAmount

def setBlcokIndexByName(chainName,redis_connect):
    if(redis_connect == None):
        print("connect is None,please check")
        pass
    if chainName == None:
        print("no such chainName")
        return -1
    else:
        nowIndex = redis_connect.get('nowIndex')
        redis_connect.set(chainName,int(nowIndex))
        redis_connect.set('nowIndex',int(nowIndex)+1)
        return nowIndex

def setBlockByIndex(chainIndex, chainNode, redis_connect):
    if(redis_connect == None):
        print("connect is None,please check")
        pass
    if chainNode == None:
        print("no such chainName")
        return -1
    if chainIndex == -1:
        print("no such chainName")
        return -1
    redis_connect.set(chainIndex+'time', chainNode.time)
    redis_connect.set(chainIndex + 'pre', chainNode.pre_hash)
    redis_connect.set(chainIndex + 'hash', chainNode.hash)
    redis_connect.set(chainIndex + 'nums', chainNode.listNum)
    return 0

def setNodeByIndex(nodeList,chainIndex,redis_connect):
    if (redis_connect == None):
        print("connect is None,please check")
        pass
    if nodeList == None:
        print("no such chainName")
        return -1
    if chainIndex == -1:
        print("no such chainName")
        return -1
    for node in nodeList:
        redis_connect.set(str(chainIndex)+'li'+str(node.index)+'act',node.data.account)
        redis_connect.set(str(chainIndex)+'li'+str(node.index)+'add',node.data.address)
        redis_connect.set(str(chainIndex)+'li'+str(node.index)+'cate',node.data.category)
        redis_connect.set(str(chainIndex)+'li'+str(node.index)+'amt',node.data.amount)
    return 0
