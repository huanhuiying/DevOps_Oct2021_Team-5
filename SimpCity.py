import random
import re
from US6and12 import *
from US7 import *
from US8 import *
from US10 import *
from us17exit import *
from us18confirmexit import *
from US13 import *

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
    choosen_configureMenu_option =  (input("Your choice? "))

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

    return grid

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
            while True:
                choosen_configureMenu_option, building_one, building_two = configure_menu(turn_counter)
                configVal = configMenuVal(choosen_configureMenu_option)
                configValBool = False
                if configVal == True:
                    continue
                else:
                    configValBool = True
                    break
            choosen_configureMenu_option = int(choosen_configureMenu_option)
            # build houses
            if choosen_configureMenu_option == 1 or choosen_configureMenu_option == 2:
                if choosen_configureMenu_option == 1:
                    building_choice = list(building_one)
                    building_name = building_one
                elif choosen_configureMenu_option == 2:
                    building_choice = list(building_two)
                    building_name = building_two
                        
                while True:
                    building_cfm = input(("Confirm using {}? [Y/N]: ").format(building_name))
                    if buildingConfirm(building_cfm):
                        continue
                    else:
                        if building_cfm.lower() == "y":
                            confirmBuildingBool = True
                            break
                        else:
                            confirmBuildingBool = False
                            break
                        
                print()      
                if not confirmBuildingBool:
                    turn_counter = turn_counter - 1
                    continue

                    
                while True:
                    location = list(input("{} ".format("Build where?")))
                    location_cfm = input(("Confirm using {} on location {}? [Y/N]: ").format(building_name,''.join(location)))
                    print()
                    if positionConfirm(location_cfm):
                        continue
                    else:
                        if location_cfm.lower()=="y": 
                            if not location_format(location):
                                print("Invalid location please try again!")
                                continue
                            else:
                                if turn_counter > 1:
                                    if not validate_location(location,grid):
                                        print("You are not able to place your building here, please try again!")
                                        continue
                                    else:
                                        break
                                else:
                                    break
                        else:
                            continue

                    
                grid = place_building(location, building_choice)

                if exitAfterGameEnd(turn_counter):
                    turn_counter = 0
                    grid = []
                    break
                    
                else:
                    cancelledTurnCount = 0
                    continue

            #[0] exit from game to main menu
            elif choosen_configureMenu_option ==0:
                exitFlag = True
                exitCount = 0
                exitInput = ""

                saveFlag = True
                saveCount = 0
                saveInput = ""

                confirmExitBool = True

                printExitPrompt(exitFlag, exitCount, exitInput)
                while True:
                    exitInput = input()
                    exitFlag, exitCount = checkUserInput(exitInput, exitCount)

                    if(exitFlag == True):
                        printExitPrompt(exitFlag, exitCount, exitInput)
                        continue
                    elif(exitFlag == False):
                        exitInputBool = checkValidInput(exitInput)
                        if(exitInputBool == True):
                            printSavePrompt(saveFlag, saveCount, saveInput)
                            while True:
                                saveInput = input()
                                saveFlag, saveCount = checkSaveInput(saveInput, saveCount)
                                if(saveFlag == True):
                                    printSavePrompt(saveFlag, saveCount, saveInput)
                                    continue
                                elif(saveFlag == False):
                                    checkValidSaveInput(saveInput)
                                    turn_counter = 0
                                    break
                            break
                        elif(exitInputBool == False):
                            print("Decision to exit game to the main menu is cancelled.")
                            confirmExitBool = False
                            break
                
                print(confirmExitBool)
                if(confirmExitBool == True):
                    turn_counter = 0
                    grid = []
                    break
                elif(confirmExitBool == False):
                    
                    turn_counter = turn_counter - 1
                    continue
            

    #load save file
    elif choosen_menu_option == 2:
        print ("Saving")
    
    #Close application
    elif choosen_menu_option == 0:
        print ("Exiting application...")
