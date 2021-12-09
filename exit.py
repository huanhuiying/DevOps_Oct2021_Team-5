#Exit Game to Menu

#US20 - As a user, I want to be able to go back to the main menu after I have ended the game.
#Write test script first, fail it then pass
# turn_counter = 0
# main_menu_options = ["Start new game", "Load saved game"]
# configure_menu_options = ["Build a HSE", "Build a BCH", "See remaining buildings", "See current score"]

flag = True
count = 0
i = ""

def printPrompt(bool, count, ipt):
    if(bool == True):
        if(count == 0):
            return print("Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")
        else:
            return print("Invalid input. Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")
    else:
        return checkUserInput(ipt)

    

def printMenu():
    return print("Menu Printed")

def validateUserInput(input, c):
    c = 1
    if(input == "Y" or input == "N"):
        print(c)
        return (False, c)
    else:
        print(c)
        return (True, c)
    


def checkUserInput(input):
    if input == 'Y':
        return printMenu()
    elif input == 'N':
        return print("Exit to main menu is cancelled.")

def exitToMenu(f, c, i):
    print(c)

    while(f):
        printPrompt(f, c,i)
        i = input()
        print(i)
        f, c = validateUserInput(i, c)
        printPrompt(f,c,i)
        if(f == False):
            print("Prompt Ended")
            break
    return 

#exitToMenu(flag,count,i)