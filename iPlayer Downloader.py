import os

def PIDDownloader():
    os.system("cls")
    print("Please enter the list of PIDs, one on each line.")
    print("Enter 'd' when finished")
    pids = []
    finished = False
    while finished == False:
        entry = input()
        if entry == "d":
            finished = True
        else:
            if entry != "":
                pids.append(entry)

    if len(pids) > 0:
        os.system("cls")
        print("I will download the following PIDs:")
        pidlist = ""
        for pid in pids:
            pidlist = pidlist + pid + ", "

        pidlist = pidlist[:-2]
        print(pidlist)
        print("")
        print("Is this correct? y or n")
        correct = input()
        correct = correct.lower()
        if correct == "y" or correct == "yes":
            os.system("cls")
            i = 1
            total = len(pids)
            for pid in pids:
                print("Downloading episode " + str(i) + " of " + str(total) + "...")
                command = "get_iplayer --overwrite --force --subtitles --subs-embed --file-prefix=\"<name> - <episode>\" --whitespace --tv-quality=fhd --pid=" + pid
                os.system(command)
                print("")
                i += 1
            
            
            print("#######################")
            print("Completed")
        else:
            print("Chose no")

    else:
        print("No PIDs entered")

    print("ENTER to continue")
    input()

def PIDInfo():
    print("Please enter the list of PIDs, one on each line.")
    print("Enter 'done' when finished")
    pids = []
    finished = False
    while finished == False:
        entry = input()
        if entry == "done":
            finished = True
        else:
            pids.append(entry)

    if len(pids) > 0:
        i = 1
        total = len(pids)
        for pid in pids:
            print("Getting episode info " + str(i) + " of " + str(total) + "...")
            command = "get_iplayer -i --pid=" + pid
            os.system(command)
            print("")
            i += 1
            
        print("#######################")
        print("Completed")
    else:
        print("No PIDs entered")
    
    print("ENTER to continue")
    input()
    

while(True):
    os.system("cls")
    print("iPlayer Downloader")
    print("")
    print("1 - PID Downloader")
    print("2 - PID Info")
    choice = input()
    if choice == "1":
        PIDDownloader()
    elif choice == "2":
        PIDInfo()