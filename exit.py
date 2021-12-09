#Exit Game to Menu

#US20 - As a user, I want to be able to go back to the main menu after I have ended the game.
#Write test script first, fail it then pass
# turn_counter = 0
# main_menu_options = ["Start new game", "Load saved game"]
# configure_menu_options = ["Build a HSE", "Build a BCH", "See remaining buildings", "See current score"]


def printPrompt(bool, count):
    return "Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: "

def printMenu():
    return "Menu Printed"

def validateUserInput(input, count):
    return


def checkUserInput(input):
    if input == 'Y':
        return printMenu()
    elif input == 'N':
        return "Exit to main menu is cancelled."
    else:
        return "Invalid input. Please enter 'Y' or 'N' to continue: "

def exitToMenu():
    printPrompt()
    emptyinput = None
    return checkUserInput(emptyinput)