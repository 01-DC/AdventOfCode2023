# full_input = open("test.txt").read().strip().split('\n')
full_input = open("input.txt").read().strip().split('\n')
digit_name_dict = {
    'o' : ['one'], 
    't' : ['two', 'three'],
    'f' : ['four', 'five'],
    's' : ['six', 'seven'],
    'e' : ['eight'],
    'n' : ['nine'],
    'z' : ['zero']
}

digit_val_dict = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    'zero' : '0'
}

total = 0
for line in full_input:
    selected_digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            selected_digits.append(c)
        elif c in digit_name_dict:
            possible_digits = digit_name_dict[c]
            for digit_name in possible_digits:
                if digit_name == line[i: i+len(digit_name)]:
                    selected_digits.append(digit_val_dict[digit_name])
    
    value = selected_digits[0] + selected_digits[-1]
    total += int(value)

print(total)