input_list = []
with open('input.txt', 'r') as file:
    for line in file:
        input_list.append([int(_) for _ in line.strip()])

total = 0
for line in input_list:
    first, second = 0, 0
    for i in range(len(line) - 1):
        if line[i] > first:
            first = line[i]
            second = 0
        if line[i + 1] > second:
            second = line[i + 1]
    total += (first * 10) + second

print(total)

