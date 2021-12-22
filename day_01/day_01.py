with open('input.txt', 'r') as file:
    depths = [int(l) for l in file.readlines()]

# Part 1
print(sum([1 for i, depth in enumerate(depths) if depth - depths[i - 1] > 0]))

# Part 2
print(sum([1 for i, depth in enumerate(depths) if (sum(depths[i-3: i]) - sum(depths[i-4:i-1])) > 0]))
