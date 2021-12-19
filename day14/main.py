from collections import Counter

with open('input') as f: input_lines = f.read()

input = input_lines.split('\n\n')
polymer = list(input[0])
instructions = [x.split(' -> ') for x in input[1].split('\n')]
d = {}
[d.update({k:v}) for k,v in instructions]

copy = polymer.copy()

steps = 10

for i in range(steps):
    new_poly = []
    for k in range(0, len(copy)-1, 1):
        str = ''.join(copy[k:k+2])
        if str in d.keys():
            polymer.insert(k+1, d[str])
            new_poly.append(copy[k])
            new_poly.append(d[str])
        else:
            new_poly.append(copy[k])
    new_poly.append(copy[len(copy)-1])
    copy = new_poly
    # print(f'Step {i}: Polymer: {new_poly}')

# print(new_poly)
# print(copy)

c = list(Counter(copy).values())
c.sort()
print(c[len(c)-1] - c[0])