#US8 - As a user, I want to be given a prompt to verify my decision 
# in placing a building so I do not accidentally place the building
#  in a position I do not want.

def positionConfirm(cfm):
    try: 
        if cfm == "Y" or cfm == "N" or cfm == "y" or cfm == "n":
            if cfm.capitalize() == "Y":
                print("Position confirmed")
                return False
            else:
                print("Cancelled")
                return False
        else:
            print("Use only 'Y' or 'N' to confirm")
            return True      
    except ValueError:
        print("Use only 'Y' or 'N' to confirm")
        return True

