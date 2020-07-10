from simple_term_menu import TerminalMenu
import netifaces, pyqrcode

def ip4_addresses():
    return [netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr'] for iface in netifaces.interfaces() if netifaces.AF_INET in netifaces.ifaddresses(iface)]

def showMenu(port):
    ipl = ip4_addresses()
    terminal_menu = TerminalMenu(ipl)
    choice_index = terminal_menu.show()
    ip = ipl[choice_index]
    url = "http://" + str(ip) + ":" + str(port)
    printQR(url)
    return ip


def printQR(urlP):
    url = pyqrcode.create(urlP)
    print(url.terminal(quiet_zone=1))

# showMenu(5000)