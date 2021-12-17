with open('input') as file:
    input_lines = file.readlines()

opening = list('([{<')
closing = list(')]}>')
stack = []

illegal_character_count = {")": 0, "]": 0, "}": 0, ">": 0}

for line in input_lines:
    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack.pop() != opening[closing.index(char)]:
                illegal_character_count[char] += 1
                break

syntax_error = [3, 57, 1197, 25137]
print(f'Syntax error score: \
{sum( [a * b  for a,b in zip(syntax_error, list(illegal_character_count.values()))] )}')