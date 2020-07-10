from os import walk, path, getcwd
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


def readFromfile(filename):
    if path.isfile(filename):
        dataList = open(filename, 'r').readlines()
    else:
        dataList = [path.abspath(getcwd())]
    print("Adding Files from {} Folders".format(len(dataList)))
    for i in dataList:
        getAllFiles(i.strip())
    print("Added {} Files ".format(len(af())))
