from Module4 import *
import NetworkAdd
import NetworkView
import Server
import Client
import ChatRoom
import Network
from socket import *
def End():
    print("End Program")
def Main():
    CmdMsg = ">>> "
    HomeComputer = gethostbyname(gethostname())
    Command = ProgramControl("LAN Comm Main Menu",["0 - End Lan Comm","1 - Network","2 - Chat Room"],CmdMsg)
#--------------------------------------------------------------------------------------------------------------------------       
    if Command == 0:# End Program
        End()
#--------------------------------------------------------------------------------------------------------------------------        
    if Command == 1:
        MainMenu = Network.Main(CmdMsg,HomeComputer)
        if MainMenu == "END":
            Main()        
#--------------------------------------------------------------------------------------------------------------------------               
    if Command == 2:# Chat Room
        MainMenu = ChatRoom.Main(CmdMsg,HomeComputer)
        if MainMenu == "END":
            Main()
#--------------------------------------------------------------------------------------------------------------------------   
Main()


