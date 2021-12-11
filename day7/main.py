# AoC - Day 7

with open('input') as file:
    initial_position = [int(x) for x in file.readline().split(',')]

maximum_position = max(initial_position)
fuel_consumption = [0 for x in range(0, maximum_position + 1, 1)]

for x in range(0, maximum_position + 1, 1):
    fuel_consumption[x] = 0
    for i in initial_position:
        delta = abs(int(i) - x)
        # part 1
        # fuel_consumption[x] += delta
        # part 2
        fuel_consumption[x] += sum(range(1, delta + 1, 1))

print(min(fuel_consumption))