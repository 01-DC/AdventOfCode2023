# 12 R
# 13 G
# 14 B

# full_input = open("test.txt").read().strip().split('\n')
full_input = open("input.txt").read().strip().split('\n')

colors_dict = {
     'red' : 12,
     'green' : 13,
     'blue' : 14
}
total = 0
for line in full_input:
    curr_game = line.split(':')
    game_id = curr_game[0].split()[-1]
    # print(game_id)
    games = [x.strip().split(', ') for x in curr_game[1].strip().split('; ')]
    # print(games)
    game_color_dict = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    for game in games:
        for g in game:
            val, col = g.split()
            game_color_dict[col] = max(game_color_dict[col], int(val))

    # print(game_color_dict)
    if game_color_dict['red'] <= colors_dict['red'] and game_color_dict['green'] <= colors_dict['green'] and game_color_dict['blue'] <= colors_dict['blue']:
        total += int(game_id)

print(total)

# print(total)