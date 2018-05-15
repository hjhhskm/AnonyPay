
list = {}
list['a'] = 0
list['b'] = 10

listNum = 100
try:
    listNum = list['nums']
except KeyError:
    listNum = 0
print(listNum)
print(str(str(listNum)))