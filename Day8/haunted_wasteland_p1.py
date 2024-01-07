import ast


move = "LRLRRRLRRLRLRRRLRRLLRRRLRLRLRLRRLRRRLRRLLRLRLRRRLRLLRRLRRLRLLRRLLRRLRRRLLRRLRRLRRRLRRRLRRRLRLRRLRRRLLRRLRRLRRRLRLRRRLRRLRRRLRRRLRLRLRLRLRLRLLRRLLLLRLRRRLRRRLLRRLRLRLLRRRLRLRRLRRRLLLLRRRLLRRLRRLRRLLRLLLLRLRRRLRLRRLRRLLRRRLRRLRLRRLRRRLLRRRLLRLRRLRRLLRRRLLRLRRLRLRRLLLRRRR"
move_low, move_high = 0, len(move)

source = 'AAA'
map_dict = {}

count = 0

with open('testcase.txt') as file:
    data = file.readlines()

    for line in data:
        line = line.strip().replace('(','').replace(')','')
        source_map, dest_to_be = line.split(' = ')
        dest_to_be =  dest_to_be.strip().replace(' ', '').split(',')

        map_dict[source_map] = dest_to_be

#print(map_dict)

dest = ''

while dest != 'ZZZ':

    print(source, dest)


    dest = map_dict[source][0] if move[move_low] == 'L' else map_dict[source][1]
    source = dest

    move_low += 1

    if move_low >= move_high:
        move_low = 0
    
    count+=1


print(count)