

def inputFunc(*kid,**kids):
    for index in kid:
        print(index)
        print("\n")
    print("_______________________")
    for now in kids:
        print("__23333____________")
        for now_now in now:
            print(now_now)
            print("\n")

node1 = ["1","2","3"]
node2 = [["4","5"],["6","7"],["8"]]
inputFunc(node1,node2)