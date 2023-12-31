"""
releasing the button allows the boat to move
the boat's speed increases by one millimeter per millisecond.
You can only hold the button at the start of the race, and boats don't move until the button is released.
For each whole millisecond you spend holding down the button, the boat's speed increases by 1 mm/ms

Dis = speed * time


Time:      7  15   30
Distance:  9  40  200

7 -> 9

time button presssed  speed*remaining_time  distance_covered
           1,             1*6 ->                 6<9           No
           2,             2*5 ->                 10>9          Yes
           3,             3*4 ->                 12>9          Yes
           4,             4*3 ->                 12>9          Yes  |    duplicate
           5,             5*2 ->                 10>9          Yes  |
           6,             6*1 ->                 6<9           No
           7,             0*0 ->                 0<9           No



"""


with open('testcase.txt')  as file:
    data  = file.readlines()

time = data[0].split(':')[1].strip().replace('  ','_').replace(' ','').split('_')
distance = data[1].split(':')[1].strip().replace('  ','_').replace(' ','').split('_')

print(time,distance)

dict_map = {}

for i in range(len(time)):
    dict_map[int(time[i])] = int(distance[i])





prod = 1

for key in dict_map.keys():
    time, distance_needed  = key, dict_map[key]
    hash_map = set()
    res = []

    for i in range(1,time):
        distance_covered = i * (time-i)
        if distance_covered > distance_needed: #and distance_covered not in hash_map:
            res.append(i)
        hash_map.add(distance_covered)
    
    tmp = len(res)
    # print(hash_map)
    # print(res)

    # ways = tmp*2 if tmp % 2 == 0 else (tmp*2)-1
    # print(ways)
    prod = prod * tmp

print(prod)