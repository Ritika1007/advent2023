import re
import math

move = "LRLRRRLRRLRLRRRLRRLLRRRLRLRLRLRRLRRRLRRLLRLRLRRRLRLLRRLRRLRLLRRLLRRLRRRLLRRLRRLRRRLRRRLRRRLRLRRLRRRLLRRLRRLRRRLRLRRRLRRLRRRLRRRLRLRLRLRLRLRLLRRLLLLRLRRRLRRRLLRRLRLRLLRRRLRLRRLRRRLLLLRRRLLRRLRRLRRLLRLLLLRLRRRLRLRRLRRLLRRRLRRLRLRRLRRRLLRRRLLRLRRLRRLLRRRLLRLRRLRLRRLLLRRRR"

move_low, move_high = 0, len(move)

map_dict = {}
source = []
with open('testcase.txt') as file:
    data = file.readlines()

    for line in data:
        source_map, left, right = re.search("(...) = \((...), (...)\)", line).groups(0)

        map_dict[source_map] = [left,right]

        if source_map[-1] == 'A':
            source.append(source_map)

print(source)


res = []



for i in source:
    dest = 'ANA'
    count = 0
    src = i
    while dest[-1] != 'Z':
        print(src,dest)
        dest = map_dict[src][0] if move[move_low] == 'L' else map_dict[src][1]

        src = dest

        move_low += 1

        if move_low >= move_high:
            move_low = 0
    
        count+=1
    
    res.append(count)
    print(res)
        
result = math.lcm(*res)
print(result)