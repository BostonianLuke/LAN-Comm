# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Author:   Luke Therieau
# Name:     Module4
#
# Description: 
# This be the module containing functions required to run Program 4, 5, and 5a.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
import random
import datetime
def readEmployeeName():
    Name = input("\nEmployee Name: ")        
    while Name == '': 
        print("Employee name must be entered")
        Name = input("Employee Name: ")
    return Name
#   readEmployerName will take in Name and validate that whats inputed is at least one character and then it will be returned.
#-----------------------------------------------------------------
def readHourlyRate():
    Valid = "F"
    while Valid == "F":
        HR = input("Hourly Rate: ")
        try:
            while HR == '' or (float(HR) < 20.00):                                             
                print("Invalid Hourly Rate, must be at least $20.00/hour")                                            
                HR = input("Hourly Rate: ")
        except ValueError:
            print("Non-numeric value entered.")
            Valid = "F"
        else:
            return float(HR)
 # This program takes in a value that is equal to the inputed Hourly Rate. It is then validated to ensure no empty spaces or a value less than 20 ($/Hr).
 # If less that 20. Than error message will appear and the user will have try again. If the value is validated and above or equal to 20 than the value of HR
 # will be returned. Alsp now ensure that any ValueError is caught.
#---------------------------------------------------------------------------------------------
def readWeeklyHours(W):
    Valid = "F"
    while Valid == "F":
        print("Enter hours worked for week",W,end="")
        Condition = input(": ")
        try:
            while Condition == "" or float(35) > float(Condition) or float(Condition) > float(80):
                print("Invalid number of hours, must be between 35 and 80")
                print("Enter hours worked for week",W,end="")
                Condition = input(": ")  
        except ValueError:
            print("Non-numeric value entered.")
            Valid = "F"
        else:
            return float(Condition)
# This program takes in value W which stands for the week that is question that will be generated
# The only thing changing in the message is the week number. Once inputed by the user the value will be validated to ensure that it fits
# the requirments. Validations are in order to ensure the hours are between 35 and 80, not blank, and also now ensures that any ValueError is caught.
#---------------------------------------------------------------------------------------------------------------------------------------------
def EnterValidateReturn(Question,Package,Order):
    Valid = "F"
    while Valid == "F":
        print(Question,end="")
        Value = input(": ")
        try:
            Index = int(0)
            while Index < len(Order):
                if Order[Index] == "Must Enter Something":
                    while Value == Package[Index]:                                             
                        print("Must Enter Something")                                            
                        print(Question,end="")
                        Value = input(": ")
                    Index += int(1)
                elif Order[Index] == "Less Than":
                    while float(Value) < Package[Index]:
                        print("Must be greator than",Package[Index])
                        print(Question,end="")
                        Value = input(": ")
                    Index += int(1)
                elif Order[Index] == "Greator Than":
                    while float(Value) > Package[Index]:
                        print("Must be less than",Package[Index])
                        print(Question,end="")
                        Value = input(": ")
                    Index += int(1)
                elif Order[Index] == "No Numeric":
                    while Value.isdigit():
                        print("Numeric values are not allowed")
                        print(Question,end="")
                        Value = input(": ")
                    Index += int(1)
        except ValueError:
            print("Non-numeric value entered.")
            Valid = "F"
        else:
            return Value 
#---------------------------------------------------------------------------------------------------------------------------------------------

def calcInvoiceTotal(TotalHours,HR):
    if TotalHours <= 160:
        InvoiceTotal = float(TotalHours) * float(HR)
        return FormatDollars(InvoiceTotal)
    else:
        InvoiceTotal = (float(HR) + (float(HR) * float(0.05))) * (float(TotalHours) - float(160)) + (float(160) * float(HR))
        return FormatDollars(InvoiceTotal)
# This fucntion takes in the Hourly Rate (inputed and validated by the user) and Total Hours.
# If Total Hours is less than or equal to 160 than RTB (Regulat Total Hours) will be equal to TH * HR and will be put into the regular format used in
# Chapter 3. Else OHR (Overtime Hourly Rate) Will be the new Hourly Rate for hours after 160. OTH (Overtime Total Hours) will be equal to Total Hours -
#  160 which will eventually be multiplied with OHR to create OTB (Overtime Total Balance) well RTB (Regular Total Balance) will be equal to the Regular HR
# multiplied by the max regular hours of 160. AD (Amount Due) is equal to the combination of RTB and OTB.)
#---------------------------------------------------------------------------------------------------------------------------------------------------
def readNextString(MyFile):
    String = MyFile.readline().rstrip('\n')
    return String
# This function reads any string varibles and returns the value stored.
#---------------------------------------------------------------------------------------------------------------------------------------------------
def readNextfloat(MyFile):
    Float = float(readNextString(MyFile))
    return Float
# This function reads any float varibles and returns the value stored orignally as an string now converted into float.
#---------------------------------------------------------------------------------------------------------------------------------------------------
def FormatDollars(DollarAmount):
    DecimalPlacedDollarAmount = format(float(DollarAmount),',.2f')
    FormattedDollarAmount = "$" + str(DecimalPlacedDollarAmount)
    return FormattedDollarAmount
# Used to format all currency values.
#---------------------------------------------------------------------------------------------------------------------------------------------------
def FormatHours(HoursAmount):
    FormattedHours = format(float(HoursAmount),'.2f')
    return FormattedHours
# Used to format all hours values with 2 decimal places.
#---------------------------------------------------------------------------------------------------------------------------------------------------
def resetBillingFile(TXT):
    SaveFile = open(TXT,"w")
    SaveFile.close()        # Will allow the current file, if it exists to be deleted in anticipation for creating a new Billing.txt file
#---------------------------------------------------------------------------------------------------------------------------------------------------
def writeBillingRecord(VALUE,TXT):
    BillingFile = open(TXT,"a")
    for Value in VALUE:
        BillingFile.write(str(Value) + '\n')
    BillingFile.close()    
# Will open the Billing.txt file, write the same record as defined above and then
# close the file. The open, write and close will happen for each employee record written to the file.
#---------------------------------------------------------------------------------------------------------------------------------------------------
def SumHours(Week1,Week2,Week3,Week4):
    TotalHours = (float(Week1)+float(Week2)+float(Week3)+float(Week4))
    return float(TotalHours)
# Used in calc TotalHours.
#---------------------------------------------------------------------------------------------------------------------------------------------------
def ProgramControl(Title,Options,CmdMsg):
    Valid = "F"
    while Valid == "F":
        print("\n" + Title + "\n")
        index = int(0)
        while index < len(Options):
            print("\t",Options[index])
            index += 1
        C = input("\n" + CmdMsg)
        try:
            while C == '' or int(C) > int(len(Options)-1) or int(C) < int(0):
                print("\n" + Title + "\n")
                index = int(0)
                while index < len(Options):
                    print("\t",Options[index])
                    index += 1
                C = input("\n" + CmdMsg)
        except ValueError:
            Valid = "F"
        else:
            return int(C)
#---------------------------------------------------------------------------------------------------------------------------------------------------
def OpenFile(File):
    try:
        MyFile = open(File, 'r')
        List = MyFile.readlines()
        MyFile.close()
        index = 0
        while index < len(List):
            List[index] = List[index].rstrip('\n')
            index += 1
        return List
    except FileNotFoundError:
        print("\n" + "This file is non-existent")
        return "non-existent"
#---------------------------------------------------------------------------------------------------------------------------------------------------
def ReadSpecificInvoice(Index,BillingList,LIST):
    RunningIndex = int(0)
    MyFile = open(File, 'r')
    List = MyFile.readlines()
    MyFile.close()
    index = 0
    while index < len(LIST):
        List[index] = List[index].rstrip('\n')
        index += 1
    print("Employee Name: ",BillingList[RunningIndex + Index])
#---------------------------------------------------------------------------------------------------------------------------------------------------
def PrintList(List,CategoryLen):
    ListLen = len(List)
    LineNum = int(ListLen/(ListLen/CategoryLen))
    Index = int(0)
    ValueSection = int(LineNum - 1)
    for Index in range(0,int(ListLen)):
        Value = (List[Index] + '\t')
        if Index < int(ValueSection) or Index > int(ValueSection):
            print(Value,end="")
        else:
            print(Value)
            ValueSection += CategoryLen            
        Index += 1
#---------------------------------------------------------------------------------------------------------------------------------------------------
def CalcList(List,Item):
    I = int(0)
    Value = float(0)
    Index = List.index(Item)
    Index = Index + 8
    while Index < len(List):
        Value += StripFormat(List[Index])
        Index += 8
        I += 1
    return float(Value)
#--------------------------------------------------------------------------------------------------------------------------------------------------
def StripFormat(FormattedValue):
    FormattedValue = FormattedValue.replace("$","")
    FormattedValue = FormattedValue.replace(",","")
    return float(FormattedValue)
#--------------------------------------------------------------------------------------------------------------------------------------------------
def PrintList(List,TitleList):
    CategoryLen = len(TitleList)
    List = TitleList + List
    ListLen = len(List)
    LineNum = int(ListLen/(ListLen/CategoryLen))
    Index = int(0)
    ValueSection = int(LineNum - 1)
    for Index in range(0,int(ListLen)):
        Value = (List[Index] + '\t')
        if Index < int(ValueSection) or Index > int(ValueSection):
            print(len(TitleList[Index]))
            print(Value,end="")
        else:
            print(Value)
            ValueSection += CategoryLen            
        Index += 1
        #  + (" " * (len(TitleList[Index]) - len(Value)))
#--------------------------------------------------------------------------------------------------------------------------------------------------
def Dice(Modifier):
    Roll = random.randint(1, 20)
    Mod = Roll + Modifier
    return int(Mod)
#--------------------------------------------------------------------------------------------------------------------------------------------------
def TimeStamp():
    currentDT = datetime.datetime.now()
    if currentDT.hour <= 12:
        Hour = str(currentDT.hour)
        Minute = str(format(currentDT.minute,"0>2d"))
        Time = [Hour,Minute,"AM"]
    else:
        Hour = str(currentDT.hour)
        Minute = str(format(currentDT.minute,"0>2d"))
        Time = [(int(Hour)-12),Minute,"PM"]    
    Time = [currentDT.month,currentDT.day,currentDT.year] + Time
    return Time
#--------------------------------------------------------------------------------------------------------------------------------------------------
def bTimeConvert(Time):
    Time = Time.split(":")
    Time = [Time[0]] + Time[1].split(" ")
    return Time
#--------------------------------------------------------------------------------------------------------------------------------------------------
def FileDelete(HomeComputer):
    File = OpenFile("Network.txt")
    if HomeComputer != "N/A":
        item_index = File.index(HomeComputer)
        item_index = item_index - 1
        Iteration = 0
        for Iteration in range (2):
            File.remove(File[int(item_index)])
            Iteration += 1
        return File

