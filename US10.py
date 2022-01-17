def validate_location(location, grid):
    nearby_locations = [] # check if building placed down are orthogonally adjacent from selected building position
    columns = ["a", "b", "c", "d"]
    column_position = [4, 10, 16, 22]
    rows = ["1", "2", "3", "4"]
    location = location[0].lower() + location[1]

    col = columns.index(location[0])

    if grid[int(location[1]) * 2][column_position[col]] != " ": # check if position has been taken
        return False

    col_row = int(location[1]) * 2
    if col + 1 < 4: # check if value is within range
        if grid[col_row][column_position[col + 1]] != " ": # check from grid that positon is not empty
            nearby_locations.append(columns[col + 1] + location[1])
    if col - 1 > -1: 
        if grid[col_row][column_position[col - 1]] != " ": 
            nearby_locations.append(columns[col - 1] + location[1])

    r = rows.index(location[1])
    if r + 1 < 4:
        row_value = int(rows[r + 1]) * 2
        if grid[row_value][column_position[col]] != " ":
            nearby_locations.append(location[0].lower() + rows[r + 1])
    if r - 1 > -1:
        row_value = int(rows[r - 1]) * 2
        if grid[row_value][column_position[col]] != " ":
            nearby_locations.append(location[0].lower() + rows[r - 1])

    if not nearby_locations: # if there are no nearby location from selected location
        return False
    else:
        return True
