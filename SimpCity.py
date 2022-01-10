import random
from US7 import *
from US8 import *

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

# Exit to game menu

def exitAfterGameEnd(tc):
    if (tc == 16):
        return True
    else:
        return False

# function is called and choosen menu option is return
while True:
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
                  cfm = input("Confirm using this building type? [Y/N]: ")
                  buildingConfirm(cfm)
              elif choosen_configureMenu_option == 2:
                  building_choice = list(building_two)
                  cfm = input("Confirm using this building type? [Y/N]: ")
                  buildingConfirm(cfm)
                    
              location = list(input("{} ".format("Build where?")))
              print()
              cfm = input("Confirm building position? [Y/N]: ")
              positionConfirm(cfm)

              place_building(location, building_choice)

              turn_counter = 16

              if exitAfterGameEnd(turn_counter):
                  turn_counter = 0
                  grid = []
                  break
                
              else:
                  continue
            
          
