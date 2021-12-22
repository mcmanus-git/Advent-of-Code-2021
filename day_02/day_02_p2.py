with open('input.txt', 'r') as file:
    moves = file.read().split()
    moves = [(moves[i], int(moves[i+1])) for i in range(0, len(moves) - 1, 2)]

aim = 0
depth = 0
horizontal = 0

for k, v in moves:
    if k == 'down':
        aim += v
    if k == 'up':
        aim -= v
    if k == 'forward':
        horizontal += v
        depth += aim * v

print(horizontal * depth)
