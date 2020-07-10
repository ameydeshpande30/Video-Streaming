from helper.version import getVersion
from flask import Flask, send_file, make_response, send_from_directory, render_template, redirect
from helper.fileOpearions import readFromfile
import sys, os
from helper.interface import showMenu
VERSION = getVersion()
if VERSION == "PORTABLE":
    from helper.portable import start as startDB, deleteTable, oneFile, getAllFiles
else:
    from helper.db import start as startDB, deleteTable, oneFile, getAllFiles

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

app = Flask(__name__, static_url_path="/static", static_folder=resource_path(
    'static'), template_folder=resource_path("templates"))

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