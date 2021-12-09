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
        checkUserInput(ipt)

    

def printMenu():
    return "Menu Printed"

def validateUserInput(input, c):
    c = 1
    if(input != "Y" and input != "N"):
        return False, c
    else:
        return True, c
    


def checkUserInput(input):
    if input == 'Y':
        return printMenu()
    elif input == 'N':
        return "Exit to main menu is cancelled."
    else:
        return "Invalid input. Please enter 'Y' or 'N' to continue: "

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

exitToMenu(flag,count,i)