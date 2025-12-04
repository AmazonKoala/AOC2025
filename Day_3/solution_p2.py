input_list = []
with open('input.txt', 'r') as file:
    for line in file:
        input_list.append([int(_) for _ in line.strip()])

total = 0
for line in input_list:
    digits = [0] * 12
    lb = 0
    for n in range(len(digits)):
        rb = len(line) - 11 + n
        lidx = 0
        for i in range(lb, rb):
            if line[i] > digits[n]:
                digits[n] = line[i]
                lidx = i
        lb = lidx + 1
    for n in range(len(digits)):
        total += digits[n] * (10 ** (len(digits) - (n + 1)))
        
print(total)

