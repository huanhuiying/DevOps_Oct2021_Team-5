
# US22 - As a user, I want to be shown a prompt to confirm my 
# choice to end the program so I don't accidentally end the program. 

def exitConfirm(cfm):
    try: 
        if cfm == "Y" or cfm == "N" or cfm == "y" or cfm == "n":
            if cfm.capitalize() == "Y":
                print("Exit confirmed. \nExiting application...")
                return (False)
            else:
                print("Exit cancelled.")
                return (False)
        else:
            print("Use only 'Y' or 'N' to confirm")
            return (True)      
    except ValueError:
        print("Use only 'Y' or 'N' to confirm")
        return (True)






