with open('Day_1/input.txt', 'r') as file:
    input_list = [line.strip() for line in file]

lock = 50
zeros = 0
for command in input_list:
    if command[0] == 'L':
        direction = -1
    else:
        direction = 1

    dist = int(command[1:])

    lock += dist * direction

    while lock < 0:
        lock += 100
    while lock > 99:
        lock -= 100
    
    if lock == 0:
        zeros += 1

print(zeros)

