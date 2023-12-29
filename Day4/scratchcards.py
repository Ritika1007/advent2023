# win num | num I have
# points double after every match
import math

sum_pt = 0 #p1
num_cards = 0 #p2
dict_cards = {}
#dict -> card_num(key) val -> [number of replicas, points of one card]

with open('testcase.txt') as file:
    data = file.readlines()

    for i,line in enumerate(data):
        card_num = i+1
        line = line.strip().split(':')[1].strip()
        # print(line)
        win_num, num = line.split('|')[0].strip().replace('  ',' ').split(' '), line.split('|')[1].strip().replace('  ',' ').split(' ') 
        match_num = list(set(win_num) & set(num))
        if len(match_num):

            # print(match_num)
            points = math.pow(2,len(match_num)-1)
            if card_num not in dict_cards:
                dict_cards[card_num] = [1,points]
            else:
                dict_cards[card_num][0] += 1
                dict_cards[card_num][1] = points
            # print(dict_cards[card_num][0])
            for k in range(0,dict_cards[card_num][0]):
                next_card = card_num+1
                for j in range(len(match_num)):
                    
                    if next_card not in dict_cards:
                        dict_cards[next_card] = [1,0]
                    else:
                        dict_cards[next_card][0] += 1
                    next_card += 1
            # print(dict_cards)
        else:
            if card_num not in dict_cards:
                dict_cards[card_num] = [1,0]
            else:
                dict_cards[card_num][0] += 1

            

# print(dict_cards)
for val in dict_cards.values():
    num_of_card, card_points = val
    num_cards += num_of_card
    sum_pt += card_points

print("card points sum", sum_pt)
print("number of cards",num_cards)
     

