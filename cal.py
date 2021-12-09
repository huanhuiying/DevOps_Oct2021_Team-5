#US19 - As a user, I want to be able to see the computation of the final score 
# so that I can understand how the points are calculated.
# def retrieveData(hseArray, facArray, shpArray, hwyArray, bchArray):
#     print("")

facArray = []
shpArray = []
hwyArray = []
bchArray = []
# def printCal():
#     hseArray = []
#     facArray = []
#     shpArray = []
#     hwyArray = []
#     bchArray = []

#     print(f"HSE: {hseArray}")

def calTotal(array):
    total = 0
    for val in array:
        total += val
    print(total)
    return total

hseArray = [1, 5, 5, 3, 3]
hsetotal = calTotal(hseArray)
factotal = calTotal(facArray)
shptotal = calTotal(shpArray)
hwytotal = calTotal(hwyArray)
bchtotal = calTotal(bchArray)

print("HSE: " + ' + '.join(map(str, hseArray)) + " = " + str(hsetotal)) 

# hseArray = [1, 5, 5, 3, 3]
# print("HSE: " + ' + '.join(map(str, hseArray)) + " = ") 