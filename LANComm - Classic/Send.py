from socket import *

def main(clientsocket,msg):
    if msg == str(0):
        print("Chat Session Ended")
    else:
        clientsocket.send(bytes(msg,"utf-8"))

