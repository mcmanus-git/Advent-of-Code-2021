import pandas as pd

# Part 1
with open('input.txt', 'r') as file:
    moves = file.read().split()
    moves = [{moves[i]: int(moves[i+1])} for i in range(0, len(moves) - 1, 2)]


df = pd.DataFrame(moves)
print(df['forward'].sum() * (df['down'].sum() - df['up'].sum()))
