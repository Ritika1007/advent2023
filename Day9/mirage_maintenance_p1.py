res = []
with open('testcase.txt') as file:
    data = file.read().strip().split('\n')

for line in data:

    inp = list(map(int,line.split(' ')))
    last_val = []

    while True:
        tmp = []
        num_zeros = 0

        for i in range(1,len(inp)):
            diff = inp[i]-inp[i-1]
            tmp.append(diff)

            if diff == 0:
                num_zeros += 1

        last_val.append(inp[-1])
        inp = tmp
        
        if num_zeros == len(tmp):
            break
    # print(last_val)
    total = sum(last_val)
    res.append(total)

# print(res)
print(sum(res))
