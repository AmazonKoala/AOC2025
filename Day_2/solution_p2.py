import re

with open("input.txt") as file:
    input_str = file.readline().strip()

input_list = input_str.split(',')
for i, e in enumerate(input_list):
    input_list[i] = [int(_) for _ in e.split('-')]

total = 0
for e in input_list:
    for r in range(e[0], e[1] + 1):
        rstr = str(r)
        for i in range((len(rstr) // 2) + 1):
            pattern = rstr[:i]
            m = rf'^(?:{pattern})+$'
            if re.match(m, rstr):
                total += r
                break

print(total)