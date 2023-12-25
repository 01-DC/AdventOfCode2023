# full_input = open('test.txt').read().strip().split('\n')
full_input = open('input.txt').read().strip().split('\n')

time_list = full_input[0].split("Time:")[1].split()
time_list = list(map(int, time_list))

dist_list = full_input[1].split("Distance:")[1].split()
dist_list = list(map(int, dist_list))

print(time_list)
print(dist_list)

ans = 1
for t, d in zip(time_list, dist_list):
    ways = 0
    for i in range(t):
        if (i*(t-i)) > d:
            ways += 1
    
    ans *= ways

print(ans)