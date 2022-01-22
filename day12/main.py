from collections import defaultdict

with open('input') as f: lines = f.readlines()
G = defaultdict(set)

for l in lines:
    v1, v2 = l.strip().split('-')
    G[v1].add(v2)

for k, val in G.copy().items():
    for v in val:
        G[v].add(k)

path = ['start']

small_caves = 0


def visit_node(vertex, _allow_duplicates=False):
    global counter
    global small_caves

    for node in G[vertex]:
        if node == 'end':
            counter += 1
        elif node.islower():
            if node not in path:
                path.append(node)
                visit_node(node, _allow_duplicates)
                path.pop()
            elif _allow_duplicates and small_caves == 0 and node != 'start':
                small_caves = 1
                path.append(node)
                visit_node(node, _allow_duplicates)
                path.pop()
                small_caves = 0
        else:
            path.append(node)
            visit_node(node, _allow_duplicates)
            path.pop()

counter = 0
visit_node('start', _allow_duplicates=False)
print(counter)
assert (counter == 5104)
counter = 0
visit_node('start', _allow_duplicates=True)
print(counter)
assert (counter == 149220)