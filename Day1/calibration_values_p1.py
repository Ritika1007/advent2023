with open("testcase.txt") as testcase:
    line = testcase.readline()
    sum = 0
    while line:
        first = 0 
        last = 0
        for s in line:
            if s.isdigit():
                first = s
                break
        for s in line[::-1]:
            if s.isdigit():
                last = s
                break
        sum += int(first+last)
        line = testcase.readline()
    print(sum)

