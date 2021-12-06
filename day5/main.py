SKIP_DIAGONALS = False

def update_point(point):
    if point in points:
        points[point] += 1
    else:
        points[point] = 1

def process_line(x1, y1, x2, y2):
    x, y = x1, y1
    update_point(f"{x},{y}")
    kx = -1 if x1 > x2 else 1
    ky = -1 if y1 > y2 else 1

    while x != x2 or y != y2:
        x = x + (x != x2) * kx
        y = y + (y != y2) * ky
        update_point(f"{x},{y}")

points = {}
count = 0

with open('input') as file:
    for input_line in file:
        s = input_line.strip().split(" -> ")
        x1, y1 = [int(x) for x in s[0].split(",")]
        x2, y2 = [int(x) for x in s[1].split(",")]
        if SKIP_DIAGONALS and not(x1 == x2 or y1 == y2):
            continue
        process_line(x1, y1, x2, y2)

for k in points.values():
    count += (k > 1)

print(count)