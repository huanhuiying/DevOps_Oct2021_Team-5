
def buildingConfirm(cfm):
    try: 
        if cfm == "Y" or cfm == "N" or cfm == "y" or cfm == "n":
            if cfm.capitalize() == "Y":
                print("Building confirmed")
                return (False)
            else:
                print("Cancelled")
                return (False)
        else:
            print("Use only 'Y' or 'N' to confirm")
            return (True)      
    except ValueError:
        print("Use only 'Y' or 'N' to confirm")
        return (True)


