# Video-Streaming

This is simple web server which allows 'mp4' and 'webm' file to stream over network.

# New Features!

  - Allows Multiple Folders
  - Prints Qr for easy access
  - Support for sqlite3

### Installation

This App requires [Python](https://www.python.org/) v3.6+ to run.

# Warning
 - If you want to use as Portable then just run code in root folder of Vidoes
 - Or you can provide all paths in file 'paths.txt'
 - Write All Folder path in a file called 'paths.txt' (Full Paths)
 - Each path on single line
 - You can also use database to reduce memory use (if you have many files)
 - It uses sqlite3 if you have 'db.txt' file in same folder
 
Install the dependencies and devDependencies and start the server.

```sh
$ git clone https://github.com/ameydeshpande30/Video-Streaming.git
$ cd Video-Streaming
$ pip3 install -r requirements.txt
$ python3 app.py
```

License
----

[MIT](LICENSE)

