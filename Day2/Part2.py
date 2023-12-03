# full_input = open("test.txt").read().strip().split('\n')
full_input = open("input.txt").read().strip().split('\n')

total = 0
for line in full_input:
    curr_game = line.split(':')
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
    total += (game_color_dict['red'] * game_color_dict['green'] * game_color_dict['blue'])

print(total)