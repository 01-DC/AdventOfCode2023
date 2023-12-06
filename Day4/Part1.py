# full_input = open('test.txt').read().strip().split('\n')
full_input = open('input.txt').read().strip().split('\n')

final_ans = 0
for line in full_input:
    line = line.split(":")[1].strip() # take out only numbers from the line

    win_num, have_num = line.split(" | ") # separate two parts of the information
    win_num = set(list(map(int, win_num.split())))
    have_num = list(map(int, have_num.split()))
    # print(win_num, have_num)

    match_count = 0
    for num in have_num:
        if num in win_num:
            match_count += 1
    
    if match_count > 0:
        final_ans += (2**(match_count-1))

print(final_ans)