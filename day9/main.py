with open('input') as file:
    input_lines = file.readlines()

y = len(input_lines)+2
ARR = []
# pad with 9s
for idx, line in enumerate(input_lines):
    ARR.insert(idx, ['9'] + list(line.strip()) + ['9'])
x = len(ARR[0])
ARR.insert(0, ['9' for x in range(x)])
ARR.insert(y+1, ['9' for x in range(x)])

risk_level = 0
for i in range(1, y-1, 1):
    for k in range(1, x-1, 1):
        if      ARR[i][k] < ARR[i][k - 1] and \
                ARR[i][k] < ARR[i][k + 1] and \
                ARR[i][k] < ARR[i - 1][k] and \
                ARR[i][k] < ARR[i + 1][k]:
            risk_level += int(ARR[i][k]) + 1
            print(ARR[i][k])
print(risk_level)