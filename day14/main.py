# Implementing using counters, much faster :)
from collections import Counter
from collections import defaultdict

with open('input') as f: file_input = f.read()
input_chunks = file_input.split('\n\n')
polymer = list(input_chunks[0])
pairs = [''.join(p) for p in zip(polymer, polymer[1:])]
instructions = [x.split(' -> ') for x in input_chunks[1].split('\n')]
rules = {k: (k[0] + v, v + k[1]) for k, v in instructions}

#TODO: Make it accept a list of steps, and produce a result list for all the steps

def calc_poly(steps):
    ctr = Counter(pairs)
    for step in range(steps):
        #This is what I am doing differently than the other guy in terms of initializing
        new_ctr = defaultdict(int)

        for k, v in ctr.items():
            new_ctr[rules[k][0]] += v
            new_ctr[rules[k][1]] += v
        ctr = new_ctr

    letters = Counter()
    for v, k in ctr.items():
        letters.update({v[0]: k})
    letters.update({polymer[-1]})
    return letters.most_common(1)[0][1] - letters.most_common()[-1][1]

print(calc_poly(40))