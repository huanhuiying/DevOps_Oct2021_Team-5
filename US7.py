def printBuildingCfm():
    cfm = input("Confirm using a building [Y/N]: ")
    return (cfm)


def checkUserInput(input):
    input = input.capitalize()
    if (input == "Y"):
        out = print("Building used")
        return(out)
    elif (input == "N"):
        out = print("Not used")
        return(out)
    else:
        out = print("Please enter only Y or N")
        return (out)

input = printBuildingCfm()
checkUserInput(input)
