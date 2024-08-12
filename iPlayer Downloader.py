import os
from pathlib import Path

def PIDDownloader():
    print("PID Downloader")
    print("Please enter the list of PIDs, one on each line.")
    print("Enter 'd' when finished")
    pids = []
    finished = False
    while finished == False:
        entry = input()
        if entry == "d":
            finished = True
        else:
            if entry != "" and not entry.isspace():
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
    print("PID Info")
    print("Please enter the list of PIDs, one on each line.")
    print("Enter 'd' when finished")
    pids = []
    finished = False
    while finished == False:
        entry = input()
        if entry == "d":
            finished = True
        else:
            if entry != "" and not entry.isspace():
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

def ShowDownloader():
    print("Show Downloader")
    print("Please enter the list of PIDs for shows, one on each line.")
    print("Enter 'd' when finished")
    pids = []
    finished = False
    while finished == False:
        entry = input()
        if entry == "d":
            finished = True
        else:
            if entry != "" and not entry.isspace():
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
                command = "get_iplayer --overwrite --force --subtitles --subs-embed --file-prefix=\"<name> - <episode>\" --pid-recursive --whitespace --tv-quality=\"fhd,hd,sd\" --pid=" + pid
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

def SearchDownloader():
    print("Search Downloader")
    print("Some commands are already preset for easy quick searching:")
    print("--type=tv,radio --listformat=\"<index>, <name>, <episode>, <channel>, <pid>\" --long")
    print("You can add your own custom parameters as part of get_iplayer:")
    print("https://github.com/get-iplayer/get_iplayer/wiki/search")
    print("")
    print("First, Enter the text to search for:")
    searchText = input()
    print()
    print("Second, Enter any extra parameters: (leave blank for none)")
    parameters = input()

    if searchText != "" and not searchText.isspace():
        os.system("cls")
        print("Searching...")
        command = "get_iplayer --type=tv,radio --listformat=\"<index>, <name>, <episode>, <channel>, <pid>\" --long \"" + searchText + "\" " + parameters
        os.system(command)
        print("")

        chosen = False
        choice = ""
        print("Would you like to download the search results? y/n")

        while(chosen == False):
            choice = input()
            choice = choice.lower()
            if choice == "y" or choice == "n":
                chosen = True
        
        if choice == "y":
            os.system("cls")
            print("Downloading programs with the following search parameters:")
            print(searchText)
            command = "get_iplayer -g --overwrite --force --subtitles --subs-embed --file-prefix=\"<name> - <episode>\" --whitespace --radio-quality=high --tv-quality=\"fhd,hd,sd\" --type=tv,radio  --long \"" + searchText + "\" " + parameters
            os.system(command)

            print("#######################")
            print("Completed")
        else:
            print("Canceling")
    else:
        print("Nothing entered")

    print("ENTER to continue")
    input()
    
def OpenRecordingsFolder():
    print("Opening Recordings folder...")
    home = str(Path.home())
    path = home + "/Desktop/iPlayer Recordings/"
    path = os.path.realpath(path)
    os.startfile(path)
    print(path)

while(True):
    os.system("cls")
    print("iPlayer Downloader")
    print()
    print("1 - PID Downloader")
    print("2 - PID Info")
    print("3 - Show Downloader")
    print("4 - Search Downloader")
    print()
    print("0 - Open Recordings folder")
    choice = input()
    if choice == "1":
        os.system("cls")
        PIDDownloader()
    elif choice == "2":
        os.system("cls")
        PIDInfo()
    elif choice == "3":
        os.system("cls")
        ShowDownloader()
    elif choice == "4":
        os.system("cls")
        SearchDownloader()
    elif choice == "0":
        os.system("cls")
        OpenRecordingsFolder()