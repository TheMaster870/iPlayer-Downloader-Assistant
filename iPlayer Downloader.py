import os

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

os.system("cls")
print("I will download the following PIDs:")
pidlist = ""
for pid in pids:
    pidlist = pidlist + pid + ", "
print(pidlist)
print("")
print("Is this correct? y or n")
correct = input()
if correct != "y":
    print("Exiting")
    exit

os.system("cls")
i = 1
total = len(pids)
for pid in pids:
    print("Downloading episode " + str(i) + " of " + str(total) + "...")
    command = "get_iplayer --overwrite --force --tv-quality=fhd --pid=" + pid
    os.system(command)
    print("")
    i += 1

print("#######################")
print("Done")
input()
