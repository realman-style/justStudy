import os


def getInFolder():
    for file in os.listdir():
        try:
            os.chdir(os.getcwd() + "/" + file)
            # print(f"cureent positon : {os.getcwd()}"

        except NotADirectoryError or FileNotFoundError: # if file not folder type
            pass

def getCurrentFilename():
    temp = 0
    loc = os.getcwd()
    for i in reversed(loc):
        if i == "/":
            break
        else:
            temp += 1
    return loc[len(loc)-temp:]

def getSlashNum(loc):
    temp = 0
    for i in loc:
        if i == "/":
            temp += 1
    return temp



def show(startSlashNum=getSlashNum(os.getcwd())):
    # x
    for file in os.listdir():
        print("|\t" * (getSlashNum(os.getcwd()) - startSlashNum) + "┣ " + f"{file}")
        try:
            os.chdir(os.getcwd() + "/" + file)
            show()
        except NotADirectoryError or FileNotFoundError:
            continue
    os.chdir(os.getcwd()[:len(os.getcwd()) - len(getCurrentFilename())]) # just escape code





startSlashNum = getSlashNum(os.getcwd())

def getAllfileinPC():
    os.chdir("/")
    show()
#
# show(startSlashNum=os.getcwd()[:len(os.getcwd()) - len(getCurrentFilename())] + "/" + "Flappybird")

show()
