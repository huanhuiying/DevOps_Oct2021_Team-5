#initate the variable turn_counter for Turn #number
turn_counter = 0

main_menu_options = ["Start new game", "Load saved game"]
configure_menu_options = ["Build a HSE", "Build a BCH", "See remaining buildings", "See current score"]

def main_menu(main_menu_options):
    for i in range (len(main_menu_options)):
        print("{}. {}".format(i+1,main_menu_options[i]))
    print()

def configure_menu(configure_menu_options):
    for i in range (len(configure_menu_options)):
       print("{}. {}".format(i+1,configure_menu_options[i]))
    print()
    
print("Welcome, mayor of Simp City")
main_menu(main_menu_options)
print("{}. {}".format("0", "Exit"))
choosen_menu_option =  int(input("Your choice? "))
print()

#Start new game
if choosen_menu_option == 1:
    print("{} {}" .format("Turn", str(turn_counter+1)))
    #code to print the sqaure buildings here
    while True:
        configure_menu(configure_menu_options)
        print()
        print("{}. {}".format("5", "Save game"))
        print("{}. {}".format("0", "Exit to main menu"))
        choosen_configureMenu_option =  int(input("Your choice? "))
        print()
        if choosen_configureMenu_option == 1:
            turn_counter = turn_counter+1 #can do in the function
            input("{} ".format("Build where?"))
            print("{} {}" .format("Turn", str(turn_counter+1)))
            #code of the function that auto-generates the housing selections and plant the building selected to the inputted location 
            print()
        if choosen_configureMenu_option == 2:
            turn_counter = turn_counter+1# can do in the function
            input("{} ".format("Build where?"))
            print("{} {}" .format("Turn", str(turn_counter+1)))
            #code of the function that auto-generates the housing selections and plant the building selected to the inputted location 
            print()
        if choosen_configureMenu_option == 3:
            #code of the function that allows the player to see the remanining building
            print()
        if choosen_configureMenu_option == 4:
            #code of the function that allows the player to check their current score
            print()
        if choosen_configureMenu_option == 5:
            #code of the function that allows the player to save their current game progress
            print()
        else:
            #code of the function that allows the player to exit to main menu
            print()

