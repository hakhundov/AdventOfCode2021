#TODO: Note: Part 2 doesn't work. (takes too long, fix it)

from collections import Counter
import time

start_time = time.time()

with open('test_input') as f: input_lines = f.read()

input = input_lines.split('\n\n')
initial_polymer = list(input[0])
instructions = [x.split(' -> ') for x in input[1].split('\n')]
d = {}
[d.update({k:v}) for k,v in instructions]

polymer = initial_polymer.copy()

steps = 10

for i in range(steps):
    new_poly = []
    for k in range(0, len(polymer) - 1, 1):
        str = ''.join(polymer[k:k + 2])
        if str in d.keys():
            new_poly.append(polymer[k])
            new_poly.append(d[str])
        else:
            new_poly.append(polymer[k])
    new_poly.append(polymer[len(polymer) - 1])
    polymer = new_poly
    # print(f'Step {i}: Polymer: {len(new_poly)}')

print("--- %s seconds ---" % (time.time() - start_time))

c = list(Counter(polymer).values())
c.sort()
print(c[len(c)-1] - c[0])