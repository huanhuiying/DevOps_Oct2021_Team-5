
def save_game(grid):
    filename = input('Enter file name to save to: ')
    fileName = str(filename+'.csv')
    file=open(fileName,'w')
    export_map = []
    for i in range (len(grid)):
        temp = ''
        for j in range(len(grid[i])):
            temp += grid[i][j]
        export_map.append(temp)
    
    for h in range(len(export_map)):
        file.write('{}\n'.format(export_map[h]))
    print('File {} created.'.format(filename))