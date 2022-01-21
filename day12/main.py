from collections import defaultdict
with open('input') as f: lines = f.readlines()
G = defaultdict(set)

for l in lines:
    v1, v2 = l.strip().split('-')
    G[v1].add(v2)

for k,val in G.copy().items():
    for v in val:
        G[v].add(k)
# print(G)

path = ['start']
counter = 0
def visit_node(vertex):
    global counter
    for node in G[vertex]:
        if node == 'end':
            counter += 1
        elif node.islower():
            if node not in path:
                path.append(node)
                visit_node(node)
                path.pop()
        else:
            path.append(node)
            visit_node(node)
            path.pop()

visit_node('start')
print(counter)