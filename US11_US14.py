no_buildings = {"BCH": 8, "FAC": 8, "HSE": 8, "SHP": 8, "HWY": 8}

# US11
def deduct_building_chosen(selected_buidling, no_buildings):
    if no_buildings[selected_buidling] != 0:
        no_buildings[selected_buidling] = no_buildings[selected_buidling] - 1
        return True
    else:
        return False

# US 14
def show_remaining_building(no_buildings):
    remaining_building_print = []
    print("Building        Remaining")
    remaining_building_print.append("Building        Remaining")
    print("--------        --------")
    remaining_building_print.append("--------        --------")
    for building in no_buildings:
        print("{}             {}".format(building, str(no_buildings[building])))
        remaining_building_print.append("{}             {}".format(building, str(no_buildings[building])))

    return remaining_building_print