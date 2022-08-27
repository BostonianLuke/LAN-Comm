from Module4 import *
def Main(CmdMsg):
    UserName = EnterValidateReturn("User Name?",[""],["Must Enter Something","No Numeric"])
    UserIP = EnterValidateReturn("IPv4 Address?",[""],["Must Enter Something","No Numeric"])
    Command = ProgramControl("Would you like to save this entry?",["0 - No","1 - Yes"],CmdMsg)
    if Command == 1:
        writeBillingRecord([UserName,UserIP],"Network.txt")
 
