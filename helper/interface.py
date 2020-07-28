import netifaces, pyqrcode
from pprint import pprint
import inquirer

def ip4_addresses():
    return [netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr'] for iface in netifaces.interfaces() if netifaces.AF_INET in netifaces.ifaddresses(iface)]


def showMenu(port):
    ipl = ip4_addresses()
    questions = [inquirer.List("ip",message="Select One IP ",choices=ipl,),]
    answers = inquirer.prompt(questions)
    ip = answers['ip']
    url = "http://" + str(ip) + ":" + str(port)
    printQR(url)
    return ip
	

	
def printQR(urlP):
    url = pyqrcode.create(urlP)
    print(url.terminal(quiet_zone=1))

#showMenu(5000)


