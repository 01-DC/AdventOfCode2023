# full_input = open("test1.txt").read().strip().split('\n')
# full_input = open("test2.txt").read().strip().split('\n')
full_input = open("input.txt").read().strip().split('\n')

directions = full_input[0]
edges = full_input[2:]
graph = {}

for e in edges:
    e = e.split(" = ")
    u = e[0]
    v = e[1].split(", ")
    graph[u] = [v[0][1:], v[1][:3]]

directions_len = len(directions)
pos = 0
cur_node = 'AAA'
steps = 0

while cur_node != 'ZZZ':
    if directions[pos]=='L':
        cur_node = graph[cur_node][0]
    else:
        cur_node = graph[cur_node][1]
    steps+=1
    pos = (pos+1)%directions_len

print(steps)


# print(directions)
# print(graph)