from os.path import isfile
def getVersion():
    if isfile("db.txt"):
        return "FULL"
    return "PORTABLE"