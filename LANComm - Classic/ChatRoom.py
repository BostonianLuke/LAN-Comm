import NetworkAdd
import NetworkView
import Server
import Client
from Module4 import *
def Main(CmdMsg,HomeComputer):
    ProgramSignal = "False"
    while ProgramSignal == "False":
        Command = ProgramControl("Chat Room",["0 - Main Menu","1 - Send Message","2 - Receive Message"],CmdMsg)
        if int(Command) == int(0):
            return "END"
        if int(Command) == int(1):
            print("0 - Main Menu")
            File = NetworkView.Main("192.168.1.13")
            Command = input(CmdMsg)
            IP = str(File[((int(Command)*2)-1)])
            ChatLog = OpenFile("Text.txt")
            if ChatLog != "non-existent":
                i = 0
                while i < len(ChatLog):
                    print(str(ChatLog[i])+"/"+str(ChatLog[i+1])+"/"+str(ChatLog[i+2]),str(ChatLog[i+3])+":"+str(ChatLog[i+4]),str(ChatLog[i+5])+":",str(ChatLog[i+6]))
                    i += 7
            Server.main(IP)
        if int(Command) == int(2):
            ChatLog = OpenFile("Text.txt")
            if ChatLog != "non-existent":
                i = 0
                while i < len(ChatLog):
                    print(str(ChatLog[i])+"/"+str(ChatLog[i+1])+"/"+str(ChatLog[i+2]),str(ChatLog[i+3])+":"+str(ChatLog[i+4]),str(ChatLog[i+5])+":",str(ChatLog[i+6]))
                    i += 7
            try:
                Client.main(HomeComputer)
            except TimeoutError: 
                print("\n" + str(File[(int(Command)*2)]) + " is currently not online")
                ProgramSignal = "False"
            except ConnectionRefusedError:
                print("\n" + "No user is currently online")
                ProgramSignal = "False"

