import os

path = f'{os.path.dirname(__file__)}/inputs/02.txt'

with open(path) as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        [a, b] = line.split()
        if a == 'A' and b == 'X':
            total += 3
        if a == 'A' and b == 'Y':
            total += 4
        if a == 'A' and b == 'Z':
            total += 8
        if a == 'B' and b == 'X':
            total += 1
        if a == 'B' and b == 'Y':
            total += 5
        if a == 'B' and b == 'Z':
            total += 9
        if a == 'C' and b == 'X':
            total += 2
        if a == 'C' and b == 'Y':
            total += 6
        if a == 'C' and b == 'Z':
            total += 7

print(total)
