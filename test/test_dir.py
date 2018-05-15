import os

def getDir():
    rootDir = "../KeyFile"

    for list in os.listdir(rootDir):
        print(list)

getDir()