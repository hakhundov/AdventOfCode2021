with open('input') as file:
    input_lines = file.readlines()

opening = list('([{<')
closing = list(')]}>')
stack = []

illegal_character_count = {")": 0, "]": 0, "}": 0, ">": 0}
incomplete_lines = []

for line in input_lines:
    incomplete_lines.append(line.strip())
    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack.pop() != opening[closing.index(char)]:
                incomplete_lines.pop()
                illegal_character_count[char] += 1
                break


syntax_error = [3, 57, 1197, 25137]
print(f'Syntax error score: \
{sum([a * b  for a,b in zip(syntax_error, list(illegal_character_count.values()))])}')
stack.clear()

# part 2 - complete incomplete lines

point_value = [1, 2, 3, 4]
total_points = []
for line in incomplete_lines:
    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            stack.pop()
    total = 0
    while len(stack) != 0:
        t = stack.pop()
        c = closing[opening.index(t)]
        total *= 5
        total += point_value[closing.index(c)]
    total_points.append(total)

total_points.sort()
mid = int((len(total_points) - 1) / 2)
print(f'Middle score is: {total_points[mid]}')
