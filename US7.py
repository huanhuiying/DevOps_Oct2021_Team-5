

# def buildingConfirm1(cfm):
#     while True:
#         cfm = input("Y/N: ")
#         try:
#             cfm = cfm.capitalize()
#             if cfm == "Y" or cfm == "N":
#                 if cfm == "Y":
#                     print("Building confirmed")
#                 else:
#                     print("Cancelled")
#                 break
#             else:
#                 print("Use only 'Y' or 'N' to confirm")   
#         except ValueError:
#             print("Use only 'Y' or 'N' to confirm:<")
#             continue

def buildingConfirm(cfm):
    try: 
        if cfm == "Y" or cfm == "N" or cfm == "y" or cfm == "n":
            if cfm.capitalize() == "Y":
                print("Building confirmed")
            else:
                print("Cancelled")
        else:
            print("Use only 'Y' or 'N' to confirm")      
    except ValueError:
        print("Use only 'Y' or 'N' to confirm :<")


#cfm = 6
#cfm = str(input("Y/N: "))
#buildingConfirm(cfm)