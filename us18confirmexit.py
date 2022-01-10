#Prompt to Confirm Exit of Game to Main Menu

from us17exit import exitToMainMenu

flag = True
count = 0
i = ""

def printExitPrompt(bool, count, ipt):
    if(bool == True):
        if(count == 0):
            return print("Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")
        else:
            return print("Invalid input. Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")
    else:
        return checkUserInput(ipt, count)

def checkSaveInput(input, c):
    c = 1
    if(input == "Y" or input == "N"):
        return False, c
    else:
        return True, c

def printSavePrompt(b, c, i):
    if(b == True):
        if(c == 0):
            return print("Please enter 'Y' to save before exiting and 'N' to exit without saving. Please note that any unsaved data will be lost: ")
        else:
            return print("Invalid input. Please enter 'Y' to save before exiting and 'N' to exit without saving. Please note that any unsaved data will be lost: ")
    else:
        return checkSaveInput(i, c)

def checkValidSaveInput(input):
    if(input == "Y"):
        #Function to save game should be placed here
        return exitToMainMenu()
    elif(input == "N"):
        return exitToMainMenu()
    

def checkValidInput(input):
    if(input == "Y"):
        return True
    elif(input == "N"):
        return False


def checkUserInput(input, c):
    c = 1
    if(input == "Y" or input == "N"):
        return False, c
    else:
        return True, c
        



