import json
import simplejson
from itertools import islice

data = {
    'index' : 1,
    'account' : "aabbcc",
    'amount' : 100.1,
    'list_nums' : 2,
    "data" :
    [{
        'list_num' : 1,
        'account' : 'aabbccc',
        'cash' : 10
    },
    {
        'list_num' : 2,
        'account' : 'bbdfd',
        'cash' : 10
    }]
}

data2 = {
    'index' : 2,
    'account' : "ggff",
    'amount' : 52,
    'list_nums' : 3,
    "data" :
    [{
        'list_num' : 1,
        'account' : 'aabbccc',
        'cash' : 10
    },
    {
        'list_num' : 2,
        'account' : 'asdb',
        'cash' : 10
    },{
        'list_num' : 3,
        'account' : 'dfddd',
        'cash' : 10
    }]
}

json_str = json.dumps(data, indent=4)
json_str2 = json.dumps(data2, indent=4)

# print(data)
# print("json test\n" + json_str)
# print(data['amount'])

file = open("../data/test.json",'w')
file.write("{\"AnonyPay\" :[")
file.write(json_str+"\n,")
file.write(json_str2)
file.write("]}")
file.close()

file = open("../data/Chain/ChainNode_1.json",'r')
lines = file.readlines()
nowdata = ""
for line in lines:
    nowdata = nowdata + line
now_json = simplejson.loads(nowdata)
now_json_data = now_json
print(now_json_data['index'])
# print(now_json_data['index'])
file.close()

# json_get = json.loads(now_data)
# print(json_get['index'])
