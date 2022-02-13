def configMenuVal(option):
    try: 
        option =int(option)
        if option==1 or option==2 or option==3 or option==4 or option==5 or option==0:
            return False
        else:
            print ("Please choose valid options.")
            return True
    except ValueError:
        print ("Please choose valid options.")
        return True

def mainMenuVal(main_option):
    try:
        main_option=int(main_option)
        if main_option==1 or main_option==2 or main_option==0:
            return False
        else:
            print("Please choose valid options.")
            return True
    except ValueError:
        print("Please choose valid options.")
        return True