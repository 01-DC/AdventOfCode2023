from math import gcd
# full_input = open("test1.txt").read().strip().split('\n')
# full_input = open("test2.txt").read().strip().split('\n')
# full_input = open("test3.txt").read().strip().split('\n')
full_input = open("input.txt").read().strip().split('\n')

directions = full_input[0]
edges = full_input[2:]
graph = {}
cur_node = []

for e in edges:
    e = e.split(" = ")
    u = e[0]
    v = e[1].split(", ")
    graph[u] = [v[0][1:], v[1][:3]]
    if u[-1] == 'A':
        cur_node.append(u)

directions_len = len(directions)
step_count = []
pos = 0
steps = 0

# while sum([int(x[-1]=='Z') for x in cur_node])!=node_len:
for id, v in enumerate(cur_node):
    pos = 0
    steps = 0
    while v[-1] != 'Z':
        if directions[pos]=='L':
            v = graph[v][0]
        else:
            v = graph[v][1]
        steps+=1
        pos = (pos+1)%directions_len
    step_count.append(steps)

lcm = 1
for i in step_count:
    lcm = lcm*i//gcd(lcm, i)

print(lcm)