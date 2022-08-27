from socket import *

def main(clientsocket,HEADERSIZE,msg):
    if msg == str(0):
        print("Chat Session Ended")
    else:
        msg = f'{len(msg):<{HEADERSIZE}}'+msg
        clientsocket.send(bytes(msg,"utf-8"))

