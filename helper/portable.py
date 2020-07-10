ALL_FILES = []
INDEX = {}
COUNTER = 0

def start():
    global ALL_FILES, INDEX, COUNTER
    ALL_FILES = []
    INDEX = {}
    COUNTER = 0

def addFile(dir, fileName):
    global ALL_FILES, INDEX, COUNTER
    COUNTER += 1
    mapFile = {}
    mapFile["id"] = COUNTER
    mapFile["dir"] = dir
    mapFile["name"] = fileName
    ALL_FILES.append(mapFile)
    INDEX[str(COUNTER)] = mapFile

def getAllFiles():
    return ALL_FILES

def oneFile(id):
    v = INDEX[str(id)]
    return v["dir"], v["name"]

def deleteTable():
    ALL_FILES = []
    INDEX = {}
    COUNTER = 0
