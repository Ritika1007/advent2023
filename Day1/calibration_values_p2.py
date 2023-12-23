digit_words = {
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9'
}
sum = 0 
with open("testcase_p2.txt") as testcase:
    for line in testcase.readlines():
        # print(line)
        first = None
        last = None
        for i,s in enumerate(line):
            if s.isdigit():
                first = s
                break
            for word in digit_words:
                if line[i:].startswith(word):
                    # print(word)
                    first = digit_words[word]
                    break
            if first:
                break

        for i in range (len(line)-1,-1,-1):
            # print(i)
            if line[i].isdigit():
                last = line[i]
                break
            for word in digit_words:
                if line[i:].startswith(word):
                    last = digit_words[word]
                    break
            if last:
                break
        print(first,last)
        sum += int(first+last)

print(sum)

