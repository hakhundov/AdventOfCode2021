from collections import defaultdict

bins = defaultdict(int)
iterations = 256

with open('input') as file:
    initial_state = file.readline().split(',')

for x in initial_state:
    bins[x] += 1

while iterations > 0:
    t = bins['0']
    bins['0'] = bins['1']
    bins['1'] = bins['2']
    bins['2'] = bins['3']
    bins['3'] = bins['4']
    bins['4'] = bins['5']
    bins['5'] = bins['6']
    bins['6'] = bins['7'] + t
    bins['7'] = bins['8']
    bins['8'] = t
    iterations -= 1

print(sum(bins.values()))