import ui.screen
import app
import multiprocessing



def startApp(root, ip, port):
    app.start(root, ip, port)



thread = ""

def stopThread():
    global thread
    thread.terminate()

def startThread(root, ip, port):
    global thread
    thread = multiprocessing.Process(target=startApp, args=(root, ip, port))
    thread.start()


def start():
    sc= ui.screen.Screen(startThread, stopThread)

start()
