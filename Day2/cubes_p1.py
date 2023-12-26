#12 red cubes, 13 green cubes, and 14 blue
#Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red

cubes_res = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
game_sum = 0
with open("testcase_p1.txt") as file:
    for line in file.readlines():
        game_no, cubes = line.split(":")
        flag = True
        for cb in cubes.split(';'):
            for c in cb.split(','):
                num, clr = c.strip().split(" ")
                if int(num) > cubes_res[clr]:
                    flag = False
                    break
            if flag == False:
                break
        if flag:
            game_sum += int(game_no.split(' ')[1])
            print(game_no)

print(game_sum) 



