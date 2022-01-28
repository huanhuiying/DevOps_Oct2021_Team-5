no_buildings = {"BCH": 8, "FAC": 0, "HSE": 8, "SHP": 8, "HWY": 8}

def show_remaining_building(no_buildings):
    print("Building        Remaining")
    print("--------        --------")
    for building in no_buildings:
        print("{}             {}".format(building, str(no_buildings[building])))

def deduct_building_chosen(selected_buidling, no_buildings):
    if no_buildings[selected_buidling] != 0:
        no_buildings[selected_buidling] = no_buildings[selected_buidling] - 1
        return True
    else:
        return False



print(deduct_building_chosen("FAC", no_buildings))
show_remaining_building(no_buildings)