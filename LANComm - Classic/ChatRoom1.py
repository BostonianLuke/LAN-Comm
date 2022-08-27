import NetworkAdd
import NetworkView
import Server
import Client
from Module4 import *
def Main(CmdMsg,HomeComputer):
    ProgramSignal = "False"
    while ProgramSignal == "False":
        print("0 - Main Menu")
        File = NetworkView.Main(HomeComputer)
        Command = input(CmdMsg)
        if int(Command) == int(0):
            return "END"
        else:
            ChatRoomSignal = "False"
            while ChatRoomSignal == "False":
                IP = str(File[((int(Command)*2)-1)])
                CommandOption = ProgramControl("Network",["0 - Chat Room Main Menu","1 - Send Message","2 - Receive Message"],CmdMsg)
                if CommandOption == 0:
                    ChatRoomSignal = "True"
                if CommandOption == 1:
                    ChatLog = OpenFile("Text.txt")
                    print(len(ChatLog))
                    i = 0
                    while i < len(ChatLog):
                        print(str(ChatLog[i])+"/"+str(ChatLog[i+1])+"/"+str(ChatLog[i+2]),str(ChatLog[i+3])+":"+str(ChatLog[i+4]),str(ChatLog[i+5])+":",str(ChatLog[i+6]))
                        i += 7
                    Server.main(IP)
                    Main()
                if CommandOption == 2:
                    ChatLog = OpenFile("Text.txt")
                    print(len(ChatLog))
                    i = 0
                    while i < len(ChatLog):
                        print(str(ChatLog[i])+"/"+str(ChatLog[i+1])+"/"+str(ChatLog[i+2]),str(ChatLog[i+3])+":"+str(ChatLog[i+4]),str(ChatLog[i+5])+":",str(ChatLog[i+6]))
                        i += 7
                    try:
                        Client.main(IP)
                    except TimeoutError:
                        print("\n" + str(File[(int(Command)*2)]) + " is currently not online")
                        ChatRoomSignal = "False"
                

