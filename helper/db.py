from peewee import *

db = SqliteDatabase('files.db')

class BaseModel(Model):
    class Meta:
        database = db

class Files(BaseModel):
    id = AutoField()
    fileDir = CharField(max_length=5000)
    fileName = CharField(max_length=5000)


def start():
    global db
    db.connect()
    db.create_tables([Files])

def addFile(fileDir, fileName):
    Files.create(fileDir=fileDir, fileName=fileName)
    db.commit()
    
def commitData():
    db.commit()

def deleteTable():
    Files.delete().execute()

def getAllFiles():
    flist = Files.select()
    files = []
    for i in flist:
        fileD = {}
        fileD["id"] = i.id
        fileD["dir"] = i.fileDir
        fileD["name"] = i.fileName
        files.append(fileD)
    return files

def oneFile(id):
    flist = Files.select().where(Files.id == id).get()
    return flist.fileDir, flist.fileName

