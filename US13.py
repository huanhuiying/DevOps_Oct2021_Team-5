def configMenuVal(option):
    try: 
        if 0 <= option <=5:
            return False
        else:
            print ("Please choose valid options.")
            return True
    except ValueError:
        print ("Please choose valid options. ")
        return True