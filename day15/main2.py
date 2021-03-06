from queue import PriorityQueue

with open('input') as file:
    input_lines = file.readlines()

y_max = len(input_lines)
ARR = []
for idx, line in enumerate(input_lines):
    ARR.insert(idx, [int(x) for x in list(line.strip())])
x_max = len(ARR[0])

for i in range(y_max, y_max*5, 1):
    ARR.insert(i, [int(x+1) for x in ARR[i-y_max]])
    for k, j in enumerate(ARR[i]):
        if j > 9:
            ARR[i][k] = 1

for j in range(0, y_max*5, 1):
    for i in range(x_max, x_max*5, 1):
        t = ARR[j][i-x_max] + 1
        if t <= 9:
            ARR[j].append(t)
        else:
            ARR[j].append(1)


def get_neighbors(cx, cy):
    return [[cx - 1, cy], [cx + 1, cy], [cx, cy - 1], [cx, cy + 1]]

goal = [(y_max * 5) - 1, (x_max * 5) - 1]

print(goal)

start = [0, 0]
frontier = PriorityQueue()
frontier.put((0, start))
cost_so_far = dict()
cost_so_far[str(start)] = 0

while not frontier.empty():
    current = frontier.get()
    if current[1] == goal:
        print(f'Reached goal. Cost = {cost_so_far[str(current[1])]}')
        break

    for next in get_neighbors(current[1][0], current[1][1]):
        if next[0] < 0 or next[1] < 0 or next[0] > y_max*5-1 or next[1] > x_max*5-1:
            continue
        new_cost = cost_so_far[str(current[1])] + ARR[next[1]][next[0]]
        if str(next) not in cost_so_far or new_cost < cost_so_far[str(next)]:
            cost_so_far[str(next)] = new_cost
            frontier.put((new_cost, next))