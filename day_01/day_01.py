with open('input.txt', 'r') as file:
    depths = file.readlines()
    depths = [int(l) for l in depths]

print(sum([1 for i, depth in enumerate(depths) if depth - depths[i - 1] > 0]))
