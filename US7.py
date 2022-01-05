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

input = printBuildingCfm()
checkUserInput(input)
