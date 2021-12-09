main_menu_options = ["Start new game", "Load saved game"]
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

# function is called and choosen menu option is return
choosen_menu_option = main_menu(main_menu_options)
   
