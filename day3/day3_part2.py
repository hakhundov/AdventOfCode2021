# AoC - Day 3

file = open("day3_input", "r")

# load input into a list
diagnostic_report = []

for line in file:
    diagnostic_report.append(line)

# TODO: There is no guarantee that there will be only one number left
def O2_generator_rating(diagnostic_report):
    idx = 0
    while len(diagnostic_report) > 1:
        tot = 0
        for word in diagnostic_report:
            tot += int(word[idx])

        if tot >= len(diagnostic_report) / 2:
            for n, word in enumerate(diagnostic_report):
                if word[idx] == '0':
                    diagnostic_report[n] = '-'
        else:
            for n, word in enumerate(diagnostic_report):
                if word[idx] == '1':
                    diagnostic_report[n] = '-'

        diagnostic_report = [x for x in diagnostic_report if x != '-']
        # print(diagnostic_report)
        idx += 1
    return int(diagnostic_report[0], 2)

# TODO: Combine these two functions
def CO2_scruber_rating(diagnostic_report):
    idx = 0
    while len(diagnostic_report) > 1:
        tot = 0
        for word in diagnostic_report:
            tot += int(word[idx])

        if tot >= len(diagnostic_report) / 2:
            for n, word in enumerate(diagnostic_report):
                if word[idx] == '1':
                    diagnostic_report[n] = '-'
        else:
            for n, word in enumerate(diagnostic_report):
                if word[idx] == '0':
                    diagnostic_report[n] = '-'

        diagnostic_report = [x for x in diagnostic_report if x != '-']
        # print(diagnostic_report)
        idx += 1
    return int(diagnostic_report[0], 2)


# Run these separately right now. Pass-by-value messes things up.
# TODO: Understand how to do this properly in Python
# print(O2_generator_rating(diagnostic_report))
print(CO2_scruber_rating(diagnostic_report))
