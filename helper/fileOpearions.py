from os import walk
from helper.db import addFile, getAllFiles as af, commitData

def getAllFiles(path):
    for (dirpath, dirnames, filenames) in walk(path):
        try:
            for i in filenames:
                if ".mp4" in str(i) or ".webm" in str(i):
                    addFile(str(dirpath), str(i))
        except Exception as e:
            print(e)
    commitData()

def getMediaFiles(paths):
    for i in paths:
        getAllFiles(i)


def readFromfile(filname):
    try:
        dataList = open(filname, 'r').readlines()
    except:
        with open(filname, 'w') as fp: 
            pass
        return
    print("Adding Files from {} Folders".format(len(dataList)))
    for i in dataList:
        getAllFiles(i.strip())
    print("Added {} Files ".format(len(af())))
