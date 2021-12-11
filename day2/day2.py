# AoC - Day 2

f = open("day2_input", "r")

horizontal = 0
depth = 0
aim = 0

for x in f:
    command = x.split()
    if command[0] == 'forward':
        horizontal = horizontal + int(command[1])
        depth = depth + aim * int(command[1])
    elif command[0] == 'up':
        aim = aim - int(command[1])
    else:
        aim = aim + int(command[1])

print(depth*horizontal)