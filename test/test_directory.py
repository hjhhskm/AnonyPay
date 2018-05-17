
def listFunc(**input):
    print(input['num1'])
    print(input['num2'])

list = {'num1' : 1,'num2' : 2}
listFunc(**list)

list['num1'] = {'num2': 1,'num3' : 2}
print(list['num1']['num2'])