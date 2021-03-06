import rsa
import time
import os
import hashlib
from base58 import *
import base64

import Server.codeCreate

def makePayAddr(publicKey):
    hash_256 = hashlib.sha3_256()
    hash_256.update(str(publicKey).encode("utf-8"))
    hash_256_value = hash_256.hexdigest()

    hash_256_2 = hashlib.sha3_256()
    hash_256_2.update(str(hash_256_value).encode('utf-8'))
    hash_256_2_value = hash_256_2.hexdigest()

    # 使用RIPEMD160对上一次结果进行运算
    rip_160 = hashlib.new("ripemd160", hash_256_2_value.encode('utf-8'))
    rip_160_value = rip_160.hexdigest()

    return rip_160_value

def createKey(name):
    (publickey, privatekey) =  rsa.newkeys(1536)
    if os.path.exists("../KeyFile/"+name):
        print("name is already exists")
        return -1
    dirName = "../KeyFile/"+name
    os.makedirs(dirName)
    timeStr = str(time.time())
    pubName = "pub_"+name+".pem"
    privName = "priv_"+name+".pem"
    addName = "add_"+name+".addr"
    with open(dirName+"/"+pubName,"w+") as pubF:
        pubF.write(publickey.save_pkcs1().decode())
        pubF.close()
    with open(dirName+"/"+privName,"w+") as privF:
        privF.write(privatekey.save_pkcs1().decode())
        privF.close()
    #create AnonyPay address
    hash_256 = hashlib.sha3_256()
    hash_256.update(str(publickey).encode("utf-8"))
    hash_256_value = hash_256.hexdigest()

    hash_256_2 = hashlib.sha3_256()
    hash_256_2.update(str(hash_256_value).encode('utf-8'))
    hash_256_2_value = hash_256_2.hexdigest()

    # 使用RIPEMD160对上一次结果进行运算
    rip_160 = hashlib.new("ripemd160", hash_256_2_value.encode('utf-8'))
    rip_160_value = rip_160.hexdigest()
    Server.codeCreate.getCountAddress(name, rip_160_value)
    with open(dirName + "/" + addName, "w+") as addF:
        addF.write(rip_160_value)
        addF.close()
    pass

#to address

def getPayAddr(name):
    with open('../KeyFile/'+name+'/add_'+name+'.addr', 'r') as f:
        addr = f.readline()
        f.close()
    return addr

def signByPriv(name,data):
    with open('../KeyFile/'+name+'/priv_'+name+'.pem', 'r') as f:
        privatekey = rsa.PrivateKey.load_pkcs1(f.read().encode())
    signature = rsa.sign(data.encode(), privatekey, 'SHA-1')
    return signature

def verifyByPub(publicKey,message,signature):
    try:
        result = rsa.verify(message.encode(),signature, publicKey)
    except rsa.pkcs1.VerificationError:
        print("verify failed")
        return False
    else:
        return result

def getPub(name):
    with open('../KeyFile/'+name+'/pub_'+name+'.pem', 'r') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read().encode())
        f.close()
    return publicKey

def getWalletAddListByName(nameList):
    AddList = []
    for name in nameList:
        AddList.append(getPayAddr(name))
    return AddList

#test
# # createKey("zhangjbd")
# data = "I love PJ very much"
# data2 = "I love PJ very very much"
# sign = signByPriv("AnonyPay",data)
# result = verifyByPub("AnonyPay",data2,sign)
#
# print(result)
# createKey("hjh")
# print(getPayAddr("hjh"))
# print(getPayAddr("ljp"))