from Module4 import *
def Main(CmdMsg):
    UserName = EnterValidateReturn("What is the User Name you would like to delete?",[""],["Must Enter Something","No Numeric"])
    File = OpenFile("Network.txt")
    if UserName != "N/A":
        item_index = File.index(UserName)
        Iteration = 0
        for Iteration in range(2):
            File.remove(File[int(item_index)])
            Iteration += 1
    resetBillingFile("Network.txt")
    i = 0
    while i < len(File):
        #print(File[i])
        writeBillingRecord([File[i]],"Network.txt")
        i += 1
    
        
