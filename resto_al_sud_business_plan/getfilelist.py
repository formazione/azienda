import os
mylist = ""
with open("filelist.txt", "w", encoding="utf-8") as file:
    for eachfile in os.listdir():
        mylist += eachfile + "\n"
    file.write(mylist)
