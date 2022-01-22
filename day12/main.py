from collections import defaultdict

with open('input') as f: lines = f.readlines()
G = defaultdict(set)

# Add all edges from the input to the adjacency list
for l in lines:
    v1, v2 = l.strip().split('-')
    G[v1].add(v2)

# Make sure that all nodes in the graph are represented in the dict
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


def count_paths(_allow_duplicates):
    global counter
    counter = 0
    visit_node('start', _allow_duplicates)
    return counter

print(f'{count_paths(_allow_duplicates=False)}')
print(f'{count_paths(_allow_duplicates=True)}')