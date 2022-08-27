from Module4 import *
from socket import *
from datetime import *
from plyer import notification
from win10toast import ToastNotifier
import Server
def main(IP):
    HEADERSIZE = 10
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((IP,2142))
    
    msg = s.recv(16)
    msg = msg.decode("utf-8")
    str(msg)
    msg = msg.lstrip("b'")
    msg = msg.rstrip("'")
    MSG = [TimeStamp()[0],TimeStamp()[1],TimeStamp()[2],TimeStamp()[3],TimeStamp()[4],TimeStamp()[5],msg]
    writeBillingRecord(MSG,"Text.txt")
    toaster = ToastNotifier()
    toaster.show_toast("LAN Comm","New Message Received")
    i = 0
    while i < len(MSG):
        print(str(MSG[i])+"/"+str(MSG[i+1])+"/"+str(MSG[i+2]),str(MSG[i+3])+":"+str(MSG[i+4]),str(MSG[i+5])+":",str(MSG[i+6]))
        i += 7

