with open('test_input') as file:
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
        if      ARR[y][x] < ARR[y][x - 1] and \
                ARR[y][x] < ARR[y][x + 1] and \
                ARR[y][x] < ARR[y - 1][x] and \
                ARR[y][x] < ARR[y + 1][x]:
            risk_level += int(ARR[y][x]) + 1
            print(ARR[y][x])
            low_points.append([x, y]) #x, y

print(low_points)
print(risk_level)