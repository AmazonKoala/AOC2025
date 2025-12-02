with open("Day_2/input.txt") as file:
    input_str = file.readline().strip()

input_list = input_str.split(',')
for i, e in enumerate(input_list):
    input_list[i] = [int(_) for _ in e.split('-')]

total = 0
for e in input_list:
    for r in range(e[0], e[1] + 1):
        rstr = str(r)
        if len(rstr) % 2 != 0:
            continue
        if rstr[:len(rstr) // 2] == rstr[len(rstr) // 2:]:
            total += r

print(total)