# full_input = open("test.txt").read().strip().split('\n')
full_input = open("input.txt").read().strip().split('\n')

total = 0
for line in full_input:
    digits = [c for c in line if c.isdigit()]
    value = digits[0] + digits[-1]
    total += int(value)

print(total)