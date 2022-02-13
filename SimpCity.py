import random
import re
from US6and12 import *
from US7 import *
from US8 import *
from US10 import *
from us17exit import *
from us18confirmexit import *
from US13 import *
from US11_US14 import *
from US22 import *
from US15andUS19 import *
from US2_16 import * 
from US23_US24 import * 
from US3 import * 

turn_counter = 0
main_menu_options = ["Start new game", "Load saved game","Show highscores"]
building_options = ["BCH", "FAC", "HSE", "SHP", "HWY"]
grid=[]

highscore_file = open("highscore.txt", "r")
highscore_file = highscore_file.read()
highscore_dict = ast.literal_eval(highscore_file)

# function for the main menu is initiated 
def main_menu(main_menu_options):
    print("Welcome, mayor of Simp City")
    print("----------------------------")
    for i in range (len(main_menu_options)):
        print("{}. {}".format(i+1,main_menu_options[i]))
    print("{}. {}".format("0", "Exit"))  
    choosen_menu_option =  input("Your choice? ")
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
    choosen_configureMenu_option =  input("Your choice? ")

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
    choosen_menu_option = (main_menu(main_menu_options))
    if choosen_menu_option == "1" or choosen_menu_option=="2":
        if choosen_menu_option == "1":
            load_file(grid)
        elif choosen_menu_option == "2":
            grid, no_buildings, turn_counter = load_saved_game(grid)
        #load game map
        no_buildings = {"BCH": 8, "FAC": 8, "HSE": 8, "SHP": 8, "HWY": 8}

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
                            deduct_validation = deduct_building_chosen(building_name, no_buildings)
                            #print(deduct_validation)
                            if deduct_validation:
                                confirmBuildingBool=True
                                break
                            else:
                                print("The building selected has been used up, please select another building!")
                                confirmBuildingBool = False
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
                    print("Final layout of Simp City:")
                    grid_view(grid)
                    #Integration of Final Score
                    hseArray = []
                    facCount = 0
                    facArray = []
                    shpArray = []
                    hwyLocArray = []
                    hwyScoreArray = []
                    bchArray = []
                    #lArray = []
                    tArray = []
                    column = [4, 10, 16, 22] #A, B, C, D
                    row = [2, 4, 6, 8]
                    for r in row:
                        for c in column:
                            loc = [c, r]
                            b = grid[r][c - 1] + grid[r][c] + grid[r][c + 1]
                            btype = findType(loc, grid)
                            if(btype == "HSE"):
                                score = getHSEScore(loc, grid)
                                hseArray.append(score)
                            elif(btype == "FAC"):
                                facCount = facCount + 1
                            elif(btype == "SHP"):
                                score = getShpScore(loc, grid)
                                shpArray.append(score)
                            elif(btype == "HWY"):
                                hwyLocArray.append(loc)
                            elif(btype == "BCH"):  
                                score = getBCHScore(loc)
                                bchArray.append(score)
                    hseTotalScore = 0
                    for i in hseArray:
                        hseTotalScore = hseTotalScore + i
                    a = getFACScoreArray(facCount)
                    if (type(a) is int):
                        if(a == 0):
                            facTotalScore = 0
                        else:
                            facArray = [a]
                            facTotalScore = getFACTotalScore(facArray)
                    else:
                        facArray = a
                        facTotalScore = getFACTotalScore(facArray)
                    shpTotalScore = 0
                    for i in shpArray:
                        shpTotalScore = shpTotalScore + i
                    hwyScoreArray = getHWYArray(hwyLocArray)
                    hwyTotalScore = getHWYTotalScore(hwyScoreArray)
                    bchTotalScore = 0
                    for i in bchArray:
                        bchTotalScore = bchTotalScore + i

                    tArray.append(hseTotalScore)
                    tArray.append(facTotalScore)
                    tArray.append(shpTotalScore)
                    tArray.append(hwyTotalScore)
                    tArray.append(bchTotalScore)

                    if(len(hseArray) == 0):
                        hseArray = [0]
                    if(len(facArray) == 0):
                        facArray = [0]
                    if(len(shpArray) == 0):
                        shpArray = [0]
                    if(len(hwyScoreArray) == 0):
                        hwyScoreArray = [0]
                    if(len(bchArray) == 0):
                        bchArray = [0]
                    printBScore(hseArray, "HSE")
                    printBScore(facArray, "FAC")
                    printBScore(shpArray, "SHP")
                    printBScore(hwyScoreArray, "HWY")
                    printBScore(bchArray, "BCH")

                    printTotalScore(tArray)
                    score = 0
                    for i in tArray:
                        score += i

                    position = check_position(score, highscore_dict)
                    if position < 11:
                        print("Congratulations! You made the high score board at position " + str(position))
                    else:
                        print("Well done! You are at position " + str(position))

                    while True:
                        name = input("Please enter your name (max 20 chars): ")
                        if check_name_input(name):
                            break
                        else:
                            print("Name input is more than 20 characters!")
                            print()
                            continue

                    highscore_dict = save_score(name, score, highscore_dict)
                    print_leaderboard(highscore_dict)
                    turn_counter = 0
                    grid = []
                    break
                    
                else:
                    cancelledTurnCount = 0
                    continue
            
            #[3] See remaining buildings
            if choosen_configureMenu_option == 3:
                show_remaining_building(no_buildings)
                turn_counter = turn_counter-1

            #[4] See current score
            if choosen_configureMenu_option == 4:
                #implement view current score (US15)
                hseArray = []
                facCount = 0
                facArray = []
                shpArray = []
                hwyLocArray = []
                hwyScoreArray = []
                bchArray = []
                #lArray = []
                tArray = []
                column = [4, 10, 16, 22] #A, B, C, D
                row = [2, 4, 6, 8]
                for r in row:
                    for c in column:
                        loc = [c, r]
                        b = grid[r][c - 1] + grid[r][c] + grid[r][c + 1]
                        btype = findType(loc, grid)
                        if(btype == "HSE"):
                            score = getHSEScore(loc, grid)
                            hseArray.append(score)
                        elif(btype == "FAC"):
                            facCount = facCount + 1
                        elif(btype == "SHP"):
                            score = getShpScore(loc, grid)
                            shpArray.append(score)
                        elif(btype == "HWY"):
                            hwyLocArray.append(loc)
                        elif(btype == "BCH"):  
                            score = getBCHScore(loc)
                            bchArray.append(score)
                hseTotalScore = 0
                for i in hseArray:
                    hseTotalScore = hseTotalScore + i
                a = getFACScoreArray(facCount)
                if (type(a) is int):
                    if(a == 0):
                        facTotalScore = 0
                    else:
                        facArray = [a]
                        facTotalScore = getFACTotalScore(facArray)
                else:
                    facArray = a
                    facTotalScore = getFACTotalScore(facArray)
                shpTotalScore = 0
                for i in shpArray:
                    shpTotalScore = shpTotalScore + i
                hwyScoreArray = getHWYArray(hwyLocArray)
                hwyTotalScore = getHWYTotalScore(hwyScoreArray)
                bchTotalScore = 0
                for i in bchArray:
                    bchTotalScore = bchTotalScore + i

                tArray.append(hseTotalScore)
                tArray.append(facTotalScore)
                tArray.append(shpTotalScore)
                tArray.append(hwyTotalScore)
                tArray.append(bchTotalScore)

                if(len(hseArray) == 0):
                    hseArray = [0]
                if(len(facArray) == 0):
                    facArray = [0]
                if(len(shpArray) == 0):
                    shpArray = [0]
                if(len(hwyScoreArray) == 0):
                    hwyScoreArray = [0]
                if(len(bchArray) == 0):
                    bchArray = [0]
                printBScore(hseArray, "HSE")
                printBScore(facArray, "FAC")
                printBScore(shpArray, "SHP")
                printBScore(hwyScoreArray, "HWY")
                printBScore(bchArray, "BCH")

                printTotalScore(tArray)
                turn_counter = turn_counter - 1
                continue

 
            
            #[5] Save game 
            if choosen_configureMenu_option == 5:
                save_game(grid)
                save_building(no_buildings)
                save_turnCount(turn_counter)
                turn_counter = turn_counter-1

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
                
                if(confirmExitBool == True):
                    turn_counter = 0
                    grid = []
                    break
                elif(confirmExitBool == False):
                    turn_counter = turn_counter - 1
                    continue
        

    #[3]leaderboard
    elif choosen_menu_option == "3":
        print_leaderboard(highscore_dict)

    #Close application
    elif choosen_menu_option == "0":
        while True:
            exitCfm = input("Exit the application? [Y/N]: ")
            if exitConfirm(exitCfm):
                continue
            else:
                if exitCfm.lower() == "y":
                    exitAppBool = True
                    break
                else:
                    exitAppBool = False
                    break
        if exitAppBool == False:
            continue
        else:
            print("Exiting Application...")
            exit()

    else:
        print("Please choose a valid option.")
        continue
