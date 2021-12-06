# Ignore this, just leaving for a personal reason

# from matplotlib import pyplot as plt

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
    print(point)
    # x = int(point.split(",")[0])
    # y = int(point.split(",")[1])
    # plt.scatter(x,y)
    if point in points:
        points[point] += 1
    else:
        points[point] = 1

#TODO: Find out why this does not count all points!
def process_line(line):
    #TODO: no need this really
    # if line[0] == line[2] and line[1] == line[3]:
    #     update_points(f"{line[0]},{line[1]}")
    if line[0] == line[2]:
        #TODO: Figure out why i did what i did here
        k = -1 if int(line[3]) - int(line[1]) < 0 else 1
        for i in range(int(line[1]), int(line[3]) + k, k):
            update_points(f"{line[0]},{i}")
    elif line[1] == line[3]:
        k = -1 if int(line[2]) - int(line[0]) < 0 else 1
        for i in range(int(line[0]), int(line[2]) + k, k):
            update_points(f"{i},{line[1]}")
    #TODO: Combine two cases
    elif line[0] > line[2]:
        k = -1 if int(line[1]) > int(line[3]) else 1
        for idx,x in enumerate(range(int(line[0]), int(line[2]) - 1, -1)):
            y = int(line[1]) + (idx * k)
            update_points(f"{x},{y}")
    else:
        k = -1 if int(line[1]) > int(line[3]) else 1
        for idx, x in enumerate(range(int(line[0]), int(line[2]) + 1, +1)):
            y = int(line[1]) + (idx * k)
            update_points(f"{x},{y}")



# h_v_lines = [end_points(line) for line in lines if is_diagonal(end_points(line))]
all_lines = [end_points(line) for line in lines]

points = {}

for l in all_lines:
    process_line(l)

# print(points)

total_points = 0
count = 0
for k in points.values():
    total_points += k
    if k >= 2:
        count += 1
print(count)
print(total_points)

# plt.show()
# for key, value in points.items():
#     if value >= 2:
#         print(key)
#         count += 1
