import random

turn_counter = 0
main_menu_options = ["Start new game", "Load saved game"]
building_options = ["BCH", "FAC", "HSE", "SHP", "HWY"]
grid=[]

# function for the main menu is initiated 
def main_menu(main_menu_options):
    print("Welcome, mayor of Simp City")
    print("----------------------------")
    for i in range (len(main_menu_options)):
        print("{}. {}".format(i+1,main_menu_options[i]))
    print("{}. {}".format("0", "Exit"))  
    choosen_menu_option =  int(input("Your choice? "))
    print()
    return (choosen_menu_option)

#function to load game map
def load_file(grid):
    file = open("game_grid.csv", "r")
    for line in file:
        line = line.strip('\n')
        grid.append(list(line))
        
    return grid
  
  
#function to print game map
def grid_view(grid):
    for i in range(len(grid)):
        line = ""
        for thing in grid[i]:
            line += thing
        print(line)
    return grid
  
# function for configure menu 
def configure_menu(turn_counter):
    configure_menu_options = ["Build a ", "Build a ", "See remaining buildings", "See current score"]
    print("{} {}" .format("Turn", str(turn_counter)))
    grid_view(grid)
    building_one = random.choice(building_options)
    building_two = random.choice(building_options)
    configure_menu_options[0] += building_one
    configure_menu_options[1] += building_two
    for i in range (len(configure_menu_options)):
       print("{}. {}".format(i+1,configure_menu_options[i]))
    print()
    print("{}. {}".format("5", "Save game"))
    print("{}. {}".format("0", "Exit to main menu"))
    choosen_configureMenu_option =  int(input("Your choice? "))

    return choosen_configureMenu_option, building_one, building_two
  
def place_building(location, building_choice):
    if location[0].lower() == "a":
        column = 4
    elif location[0].lower() == "b":
        column = 10
    elif location[0].lower() == "c":
        column = 16
    elif location[0].lower() == "d":
        column = 22

    row = int(location[1]) * 2

    grid[row][column - 1] = building_choice[0]
    grid[row][column] = building_choice[1]
    grid[row][column +1] = building_choice[2]

#Exit Game to Menu

#US20 - As a user, I want to be able to go back to the main menu after I have ended the game.
#Write test script first, fail it then pass


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
        return False, c
    else:
        print(c)
        return True,c
    


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

# function is called and choosen menu option is return
choosen_menu_option = main_menu(main_menu_options)

if choosen_menu_option == 1:
    #load game map
    load_file(grid)

    while True:
      turn_counter = turn_counter + 1
      choosen_configureMenu_option, building_one, building_two = configure_menu(turn_counter)
      if choosen_configureMenu_option == 1 or choosen_configureMenu_option == 2:
          if choosen_configureMenu_option == 1:
              building_choice = list(building_one)
          elif choosen_configureMenu_option == 2:
              building_choice = list(building_two)
                
          location = list(input("{} ".format("Build where?")))
          print()
            
          place_building(location, building_choice)
            
          continue
