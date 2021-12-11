# AoC - Day 3

file = open("day3_input", "r")
# sample input 110111110001
total_lines = 0

hist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for word in file:
    for k, bit in enumerate(word):
        if bit == '\n':
            break
        hist[k] = hist[k] + int(bit)
    total_lines += 1

for x in hist:
    print(x)

gamma_rate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilon_rate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for k, x in enumerate(hist):
    if x > total_lines / 2:
        gamma_rate[k] = 1
print(gamma_rate)

gamma_rate_str = ""
epsilon_rate_str = ""
for x in gamma_rate:
    gamma_rate_str += str(x)
    epsilon_rate_str += '1' if x == 0 else '0'


print(gamma_rate_str)
print(epsilon_rate_str)

print(int(gamma_rate_str, 2) * int(epsilon_rate_str, 2))