from Module4 import *
def Main(HomeComputer):
    try:
        File = OpenFile("Network.txt")
        if File != "non-existent":
            item_index = File.index(HomeComputer)
            item_index = item_index - 1
            Iteration = 0
            for Iteration in range(2):
                File.remove(File[int(item_index)])
                Iteration += 1
            i = 0
            ii = 1
            while i < len(File):
                print(str(ii)+" - "+str(File[i]))
                i += 2
                ii += 1
            return File
    except ValueError:
        print("Your computer's IPv4 Address '" + HomeComputer + "'has not been added to the network")
        return int(0)
