
main_menu_options = ["Start new game", "Load saved game"]
configure_menu_options = ["Build a HSE", "Build a BCH", "See remaining buildings", "See current score"]
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

# function for configure menu 
def configure_menu(configure_menu_options):
    for i in range (len(configure_menu_options)):
       print("{}. {}".format(i+1,configure_menu_options[i]))
    print()

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

# function is called and choosen menu option is return
choosen_menu_option = main_menu(main_menu_options)

if choosen_menu_option == 1:
    #load game map
    load_file(grid)

    while True:
        #print game map
        grid_view(grid)
        configure_menu(configure_menu_options)
        print()
        print("{}. {}".format("5", "Save game"))
        print("{}. {}".format("0", "Exit to main menu"))
        choosen_configureMenu_option =  int(input("Your choice? "))
        print()
