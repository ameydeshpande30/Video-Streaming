from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import os
import pyqrcode, png, tempfile, os
from pyqrcode import QRCode 
from helper.interface import ip4_addresses
class Screen:
    def __init__(self, startThread, stopThread):
        self.startThread = startThread
        self.stopThread = stopThread
        self.master = Tk()
        self.WIDTH = "500"
        self.HEIGHT = "200"

        self.master.title("Video Stream")
        self.master.minsize(self.WIDTH, self.HEIGHT)
        self.master.maxsize(self.WIDTH, self.HEIGHT)
        self.FOLDER_NAME = str(os.path.dirname(os.path.abspath(__file__)))


        #First Row

        self.f1 = LabelFrame(self.master, text="Folder", padx=10, pady=5, width=self.WIDTH, height=2)
        self.l1 = Label(self.f1, text=self.FOLDER_NAME, borderwidth=2, background="white", relief="groove", padx=10, pady=5)
        self.b1 = Button(self.f1, text ="Change", command = self.open_file,  padx=10, pady=5)
        self.l1.pack(side="left", fill=BOTH, padx=10,expand=True)
        self.b1.pack(side="right")
        self.f1.pack(fill=BOTH, padx=20, pady=5 )


        #second Row
        self.IP = ip4_addresses()
        self.variable = StringVar(self.master)
        self.variable.set(self.IP[0])
        self.f21 = LabelFrame(self.master, text="IP and Port", padx=10, pady=5, width=self.WIDTH, height=2)
        self.l21 = Label(self.f21, text="IP : ")
        self.l21.pack(side="left")
        self.op21 = OptionMenu(self.f21, self.variable, *self.IP)
        self.op21.pack(side="left")
        self.sp21 = Spinbox(self.f21, width=15, from_=5000, to=6000)
        self.sp21.pack(side="right")
        self.l22 = Label(self.f21, text="Port : ")
        self.l22.pack(side="right")
        self.f21.pack(fill=BOTH, padx=20, pady=5)


        #third Row
        self.sbt = Button(self.master, text ="Start", command = self.start)
        self.sbt.pack(pady=10)

        self.master.mainloop()

    def clear(self):
        list = self.master.pack_slaves()
        for l in list:
            l.destroy()

    def open_file(self):
        foldername = filedialog.askdirectory()
        self.l1.config(text=foldername)
        self.FOLDER_NAME = foldername

    def genrateQR(self, uri, filname):
        url = pyqrcode.create(uri) 
        path = os.path.join(tempfile.gettempdir(), filname)
        url.png(path, scale = 8)
        return path

    def stop(self):
        self.stopThread()
        self.master.quit()

    def run(self):
        filname = "nowQR.png"
        URI = "http://{}:{}".format(str(self.ip), str(self.port))
        path = self.genrateQR(URI, filname)
        self.startTinknter(path, self.master)

    def startTinknter(self, imagePath, master):
        # self.master = Tk()
        image = Image.open(imagePath)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.master, image=photo)
        label.image = photo # keep a reference!
        label.pack(pady=20)
        bt = Button(text="Stop", command=self.stop)
        bt.pack()

    def newWindow(self):
        self.clear()
        self.WIDTH = "350"
        self.HEIGHT = "400"
        self.master.minsize(self.WIDTH, self.HEIGHT)
        self.master.maxsize(self.WIDTH, self.HEIGHT)
        self.run()

    def start(self):
        PATH = self.FOLDER_NAME
        IP = self.variable.get()
        PORT = self.sp21.get()
        self.clear()
        self.ip = IP
        self.port = PORT
        self.startThread(PATH, IP, PORT)
        self.newWindow()
        

def goAhead():
    print("bye")
# sc = Screen1(goAhead)

    