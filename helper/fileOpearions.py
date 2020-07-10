from helper.version import getVersion
from os import walk, path, getcwd
VERSION = getVersion()
if VERSION == "PORTABLE":
    from helper.portable import addFile, getAllFiles as af
else:
    from helper.db import addFile, getAllFiles as af

def getAllFiles(path):
    for (dirpath, dirnames, filenames) in walk(path):
        try:
            for i in filenames:
                if ".mp4" in str(i) or ".webm" in str(i):
                    addFile(str(dirpath), str(i))
        except Exception as e:
            print(e)

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