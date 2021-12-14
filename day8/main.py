# count = 0
# for line in input_lines:
#     s1, s2 = line.split('|')
#     for digit in s2.strip().split(' '):
#         if len(digit) in (2, 4, 3, 7):
#             count += 1
# print(count)

def map_segments():
    # [top, top_left, top_right, middle, bottom_left, bottom, bottom_right ]
    final_digits = ['-', '-', '-', '-', '-', '-', '-']
    digits = [x for x in s1.strip().split()]
    digits.sort(key=len)
    # print(digits)
    digit_mapping = {}
    digit_mapping[digits[0]] = 1
    digit_mapping[digits[1]] = 7
    digit_mapping[digits[2]] = 4
    digit_mapping[digits[9]] = 8
    # print(digit_mapping)
    final_digits[2] = final_digits[6] = set(digits[0])
    final_digits[0] = set(digits[1]).difference(final_digits[2])
    final_digits[1] = final_digits[3] = set(digits[2]) - final_digits[2]
    final_digits[4] = final_digits[5] = set(digits[9]) - final_digits[0] - final_digits[1] - final_digits[2]
    intersection_six = set(digits[6]).intersection(set(digits[7]), set(digits[8])) - final_digits[0]
    final_digits[1] = intersection_six.intersection(final_digits[1])
    final_digits[3] -= final_digits[1]
    intersection_six -= final_digits[1]
    final_digits[6] = intersection_six.intersection(final_digits[6])
    final_digits[2] -= final_digits[6]
    intersection_six -= final_digits[6]
    final_digits[5] = intersection_six
    final_digits[4] -= intersection_six
    for idx, d in enumerate(digits):
        # zero is where no middle
        if (len(d) == 6) and final_digits[3].issubset(set(d)) == False:
            digit_mapping[d] = 0
        # six is where no top_right
        if (len(d) == 6) and final_digits[2].issubset(set(d)) == False:
            digit_mapping[d] = 6
        # nine is where no bottom_left
        if (len(d) == 6) and final_digits[4].issubset(set(d)) == False:
            digit_mapping[d] = 9
        if len(d) == 5 and final_digits[1].issubset(set(d)) == True:
            # 5 has top left
            digit_mapping[d] = 5
        if len(d) == 5 and final_digits[4].issubset(set(d)) == True:
            # 2 has bottom left
            digit_mapping[d] = 2
        if len(d) == 5 and final_digits[2].issubset(set(d)) == True and final_digits[6].issubset(set(d)) == True:
            # 3 has top and bottom right
            digit_mapping[d] = 3
    return digit_mapping

def decode_value(encoded_value, a_dict):
    # print(encoded_value)
    for key in a_dict:
        if set(encoded_value) == set(key):
            return str(a_dict[key])


with open('input') as file:
    input_lines = file.readlines()

SUM = 0
for line in input_lines:
    s1, s2 = line.split('|')
    mapping = map_segments()
    print(s2, end=' ')
    output_value = [x for x in s2.strip().split()]
    out = ''
    for x in output_value:
        out += decode_value(x, mapping)
    print(out)
    SUM += int(out)
    # print(decode_value('abd', mapping))

print(SUM)