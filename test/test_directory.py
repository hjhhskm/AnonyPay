
def listFunc(**input):
    print(input['num1'])
    print(input['num2'])

list = {'num1' : 1,'num2' : 2}
listFunc(**list)