from Module4 import *
import NetworkAdd
import NetworkView
import Server
import Client
import ChatRoom
import NetworkEdit
def Main(CmdMsg,HomeComputer):
    ProgramSignal = "False"
    while ProgramSignal == "False":
        Command = ProgramControl("Network",["0 - Main Menu","1 - View Network","2 - Edit Network"],CmdMsg)
        if Command == 0:
            return "END"
        if Command == 1:
            print("0 - Network Main Menu")
            NetworkView.Main(HomeComputer)
            CommandOption = input(CmdMsg)
            if CommandOption == 0:
                ProgramSignal = "False"  
        if Command == 2:
            Command = ProgramControl("Edit Network",["0 - Main Menu","1 - Add New User","2 - Edit User"],CmdMsg)
            if Command == 0:
                ProgramSignal = "False"
            if Command == 1:
                NetworkAdd.Main(CmdMsg)
                Command = ProgramControl("Would you like to add another user?",["0 - No","1 - Yes"],CmdMsg)
                if Command == 0:
                    ProgramSignal = "False"  
                if Command == 1:
                    NetworkAdd.Main(CmdMsg)
            if Command == 2:
                NetworkEdit.Main(CmdMsg) 
