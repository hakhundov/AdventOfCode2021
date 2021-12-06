# from matplotlib import pyplot as plt

with open('input') as f: input_lines = f.read()

lines = input_lines.split('\n')


def end_points(raw_end_points):
    s = raw_end_points.replace(" ", "").split("->")
    return s[0].split(",") + s[1].split(",")


def update_points(point):
    # x = int(point.split(",")[0])
    # y = int(point.split(",")[1])
    # plt.scatter(x,y)
    if point in points:
        points[point] += 1
    else:
        points[point] = 1


def process_line(line):
    x, y = int(line[0]), int(line[1])
    update_points(f"{x},{y}")
    kx = -1 if int(line[0]) > int(line[2]) else 1
    ky = -1 if int(line[1]) > int(line[3]) else 1

    while x != int(line[2]) or y != int(line[3]):
        x = x + (x != int(line[2])) * kx
        y = y + (y != int(line[3])) * ky
        update_points(f"{x},{y}")

# h_v_lines = [end_points(line) for line in lines if is_diagonal(end_points(line))]
all_lines = [end_points(line) for line in lines]

points = {}

for l in all_lines:
    process_line(l)

count = 0
for k in points.values():
        count += (k > 1)

print(count)