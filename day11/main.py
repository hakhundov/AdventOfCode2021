with open('input') as file:
    input_lines = file.readlines()

y_max = len(input_lines) + 2
ARR = []
for idx, line in enumerate(input_lines):
    ARR.insert(idx, ['-'] + [int(x) for x in list(line.strip())] + ['-'])
x_max = len(ARR[0])
ARR.insert(0, ['-' for i in range(x_max)])
ARR.insert(y_max + 1, ['-' for i in range(x_max)])

count = 0
steps = 100

def get_neighbors(cy, cx):
    return [[cy - 1, cx], [cy + 1, cx], [cy, cx - 1], [cy, cx + 1],
            [cy - 1, cx - 1], [cy - 1, cx + 1], [cy + 1, cx - 1], [cy + 1, cx + 1]]

def increase_energy_levels():
    for y in range(1, y_max - 1, 1):
        for x in range(1, x_max - 1, 1):
            ARR[y][x] += 1

def check_energy_levels():
    for y in range(1, y_max - 1, 1):
        for x in range(1, x_max - 1, 1):
            if ARR[y][x] > 9:
                flash(y, x)

def flash(y, x):
    global count
    count += 1
    ARR[y][x] = 0
    for point in get_neighbors(y, x):
        if ARR[point[0]][point[1]] != '-' and ARR[point[0]][point[1]] != 0:
            ARR[point[0]][point[1]] += 1
            if ARR[point[0]][point[1]] > 9:
                flash(point[0], point[1])

for i in range(steps):
    increase_energy_levels()
    check_energy_levels()

print(count)