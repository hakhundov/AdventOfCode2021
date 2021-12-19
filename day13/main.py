with open('small_input') as f: input_lines = f.read()

input = input_lines.split('\n\n')

# points = [x for x in input[0].split('\n')]
# folds = [x for x in input[1].replace('fold along ', '').split('\n')]

points = [(int(x.split(',')[0]), (int(x.split(',')[1]))) for x in input[0].split('\n')]
folds = [(x.split('=')[0], int(x.split('=')[1])) for x in input[1].replace('fold along ', '').split('\n')]

# print(set(points))
new_points = []

for f in folds:
    for p in points:
        if f[0] == 'x':
            if p[0] < f[1]:
                new_points.append((p[0], p[1]))
            if p[0] > f[1]:
                new_x = 2 * f[1] - p[0]
                new_points.append((new_x, p[1]))
        if f[0] == 'y':
            if p[1] < f[1]:
                new_points.append((p[0], p[1]))
            if p[1] > f[1]:
                new_y = 2 * f[1] - p[1]
                new_points.append((p[0], new_y))

print(new_points)

print(f'Total: {len(set(new_points))}')