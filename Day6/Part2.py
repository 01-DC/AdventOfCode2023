# full_input = open('test.txt').read().strip().split('\n')
full_input = open('input.txt').read().strip().split('\n')

time_list = full_input[0].split("Time:")[1].split()
time_val = int(''.join(time_list))

dist_list = full_input[1].split("Distance:")[1].split()
dist_val = int(''.join(dist_list))

print(time_val)
print(dist_val)

ways = 0
for i in range(time_val):
    if (i*(time_val-i)) > dist_val:
        ways += 1

print(ways)