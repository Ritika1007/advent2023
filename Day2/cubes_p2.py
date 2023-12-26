gsum = 0

with open('testcase_p1.txt') as f:
    for line in f.readlines():
        game_no, cubes = line.split(":")
        clr_dict = {} 
        for cb in cubes.split(';'):
            for c in cb.split(','):
                num, clr = c.strip().split(" ")
                clr_dict[clr] = int(num) if clr not in clr_dict else max(clr_dict[clr],int(num))
        print(clr_dict)
        result = 1
        for key in clr_dict:
            result = result * clr_dict[key]
        gsum+=result

print(gsum)