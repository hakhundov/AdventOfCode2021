with open('input') as file:
    input_lines = file.readlines()

opening = list('([{<')
closing = list(')]}>')

illegal_character_count = {")": 0, "]": 0, "}": 0, ">": 0}
point_value = [1, 2, 3, 4]

stack = []
total_points = []

for line in input_lines:
    stack.clear()
    flag = True
    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack.pop() != opening[closing.index(char)]:
                illegal_character_count[char] += 1
                flag = False
                break
    if flag:
        total = 0
        while len(stack) != 0:
            t = stack.pop()
            c = closing[opening.index(t)]
            total *= 5
            total += point_value[closing.index(c)]
        total_points.append(total)

syntax_error = [3, 57, 1197, 25137]
print(f'Syntax error score: {sum([a * b  for a,b in zip(syntax_error, list(illegal_character_count.values()))])}')

total_points.sort()
mid = int((len(total_points) - 1) / 2)
print(f'Middle score is: {total_points[mid]}')