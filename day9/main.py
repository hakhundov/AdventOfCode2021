import queue
import math

with open('input') as file:
    input_lines = file.readlines()

y_max = len(input_lines) + 2
ARR = []
# pad with 9s
for idx, line in enumerate(input_lines):
    ARR.insert(idx, ['9'] + list(line.strip()) + ['9'])
x_max = len(ARR[0])
ARR.insert(0, ['9' for i in range(x_max)])
ARR.insert(y_max + 1, ['9' for i in range(x_max)])

low_points = []

risk_level = 0
for y in range(1, y_max - 1, 1):
    for x in range(1, x_max - 1, 1):
        if ARR[y][x] < ARR[y][x - 1] and \
                ARR[y][x] < ARR[y][x + 1] and \
                ARR[y][x] < ARR[y - 1][x] and \
                ARR[y][x] < ARR[y + 1][x]:
            risk_level += int(ARR[y][x]) + 1
            print(ARR[y][x])
            low_points.append([y, x])

print(risk_level)


# part 2
def get_neighbors(cx, cy):
    return [[cx - 1, cy], [cx + 1, cy], [cx, cy - 1], [cx, cy + 1]]


frontier = queue.Queue()
reached = []


def count_bredth(seed):
    frontier.put(seed)
    reached.append(seed)
    count = 0
    while not frontier.empty():
        current = frontier.get()
        count += 1
        for next in get_neighbors(current[0], current[1]):
            if next not in reached and int(ARR[next[0]][next[1]]) != 9:
                frontier.put(next)
                reached.append(next)
    return count

depth_counts = []
for point in low_points:
    c = count_bredth(point)
    depth_counts.append(c)

depth_counts.sort(reverse=True)
print(math.prod(depth_counts[0:3]))