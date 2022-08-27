from socket import *
import Send
def main(IP):
    IP = gethostname()
    s = socket(AF_INET,SOCK_STREAM)
    s.bind((IP,2142))
    s.listen(5)
    while True:
        clientsocket, address = s.accept()
        msg = ""
        while msg != str(0):
            msg = input(">>> ")
            Send.main(clientsocket,msg)
            msg = str(0)
        break
        
