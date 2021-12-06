def update_point(point):
    if point in points:
        points[point] += 1
    else:
        points[point] = 1


def process_line(line):
    x, y = int(line[0]), int(line[1])
    update_point(f"{x},{y}")
    kx = -1 if int(line[0]) > int(line[2]) else 1
    ky = -1 if int(line[1]) > int(line[3]) else 1

    while x != int(line[2]) or y != int(line[3]):
        x = x + (x != int(line[2])) * kx
        y = y + (y != int(line[3])) * ky
        update_point(f"{x},{y}")


points = {}
count = 0


with open('input') as f:
    for line in f:
        s = line.strip().split(" -> ")
        x1, y1, x2, y2 = s[0].split(",") + s[1].split(",")
        process_line([x1, y1, x2, y2])


for k in points.values():
        count += (k > 1)

print(count)
# h_v_lines = [end_points(line) for line in lines if is_diagonal(end_points(line))]
#all_lines = [end_points(line) for line in lines]