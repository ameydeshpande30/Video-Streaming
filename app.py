from flask import Flask, send_file, make_response, send_from_directory, render_template, redirect
from helper.fileOpearions import readFromfile
app = Flask(__name__)
import sys
from helper.interface import showMenu
from helper.db import start as startDB, deleteTable, oneFile, getAllFiles


@app.route("/video/<int:id>")
def send_file_V(id):
    try:
        dirv, filename = oneFile(id)
    except Exception as e:
        redirect("/")
    return send_from_directory(dirv, filename)

@app.route("/")
def index():
    fl = getAllFiles()
    return render_template("index.html", data=fl)


def start():
    startDB()
    deleteTable()
    readFromfile("paths.txt")
    port = 5000
    ip = showMenu(port)
    app.run(host=ip, port=port, threaded=True)

start()