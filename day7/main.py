# AoC - Day 7

with open('input') as file:
    initial_position = [int(x) for x in file.readline().split(',')]

maximum = max(initial_position)
fuel_consumption = [0 for x in range(0, maximum+1, 1)]

for x in range(0, maximum+1, 1):
    fuel_consumption[x] = 0
    for i in initial_position:
        fuel_consumption[x] += abs(int(i) - x)

print(min(fuel_consumption))