with open('input') as f: input_lines = f.read()

lines = input_lines.split('\n')


def end_points(raw_end_points):
    s = raw_end_points.replace(" ", "").split("->")
    return s[0].split(",") + s[1].split(",")


def is_diagonal(line_end_points):
    if (line_end_points[0] == line_end_points[2]) or (line_end_points[1] == line_end_points[3]):
        return True
    return False


def update_points(point):
    if point in points:
        points[point] += 1
    else:
        points[point] = 1


def process_line(line):
    if line[0] == line[2]:
        k = -1 if int(line[3]) - int(line[1]) < 0 else 1
        for i in range(int(line[1]), int(line[3]) + k, k):
            update_points(f"{line[0]},{i}")
    else:
        k = -1 if int(line[2]) - int(line[0]) < 0 else 1
        for i in range(int(line[0]), int(line[2]) + k, k):
            update_points(f"{i},{line[1]}")


h_v_lines = [end_points(line) for line in lines if is_diagonal(end_points(line))]

points = {}

for l in h_v_lines:
    process_line(l)

count = 0
for k in points.values():
    if k >= 2:
        count += 1

print(count)