from collections import Counter
import time
import concurrent.futures

start_time = time.time()

with open('input') as f: input_lines = f.read()

input = input_lines.split('\n\n')
initial_polymer = list(input[0])
instructions = [x.split(' -> ') for x in input[1].split('\n')]
d = {}
[d.update({k:v}) for k,v in instructions]

polymer = initial_polymer.copy()

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i * length // wanted_parts: ((i + 1) * length // wanted_parts)+1] for i in range(wanted_parts)] # added + 1 to get overallping chunks

def consturct_new_poly(polymer):
    new_poly = []
    for k in range(0, len(polymer) - 1, 1):
        str = ''.join(polymer[k:k + 2])
        if str in d.keys():
            new_poly.append(polymer[k])
            new_poly.append(d[str])
        else:
            new_poly.append(polymer[k])
    new_poly.append(polymer[len(polymer) - 1])
    return new_poly


steps = 40

if __name__ == '__main__':
    for i in range(steps):
        print(f'Performing step {i}', end=' ')
        print("%s seconds" % (time.time() - start_time))
        # polymer = consturct_new_poly(polymer)
        # print(f'Step {i}: Polymer: {len(new_poly)}')
        with concurrent.futures.ProcessPoolExecutor() as executor:

            segments = split_list(polymer, wanted_parts=16) # this basically determines the number of processes to be run...
            # print(segments)
            results = [exedaycutor.submit(consturct_new_poly, segment) for segment in segments]
            temp = polymer.pop() # save the last element in the initial polymer to be appended later
            polymer = []
            for f in concurrent.futures.as_completed(results):
                f.result().pop() # remove last element since it is overlapping
                polymer.extend(f.result())
                # print(f'results: {f.result()}')
            polymer.append(temp)
            # print(f'recunstructed new polymer: {polymer}')

    print("--- %s seconds ---" % (time.time() - start_time))
    c = list(Counter(polymer).values())
    c.sort()
    print(c[len(c)-1] - c[0])