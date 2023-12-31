with open('testcase.txt')  as file:
    data  = file.readlines()

time = int(data[0].split(':')[1].strip().replace(' ', ''))
distance = int(data[1].split(':')[1].strip().replace(' ', ''))

print(time,distance)


for i in range(1,time):
        distance_covered = i * (time-i)
        if distance_covered > distance:
            ways = ((time-i) -i) +1
            break
print(ways)