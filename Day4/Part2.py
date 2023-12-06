# full_input = open('test.txt').read().strip().split('\n')
full_input = open('input.txt').read().strip().split('\n')

num_cards = len(full_input)
card_count_arr = [1]*num_cards
print("Number of cards", num_cards)

for idx, line in enumerate(full_input):
    line = line.split(":")[1].strip() # take out only numbers from the line

    win_num, have_num = line.split(" | ") # separate two parts of the information
    win_num = set(list(map(int, win_num.split())))
    have_num = list(map(int, have_num.split()))
    # print(win_num, have_num)

    match_count = 0
    for num in have_num:
        if num in win_num:
            match_count += 1
    
    for i in range(idx+1, idx+match_count+1):
        card_count_arr[i] += (card_count_arr[idx])
    # print(card_count_arr)

print(sum(card_count_arr))