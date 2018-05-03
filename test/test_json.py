import json
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

json_str = json.dumps(data)
json_str2 = json.dumps(data2)

# print(data)
# print("json test\n" + json_str)
# print(data['amount'])

file = open("../data/test.json",'w')
file.write(json_str+"\n")
file.write(json_str2)
file.close()

file = open("../data/test.json",'r')
now_data = file.next()
file.close()
print(now_data)
