import os

path = f'{os.path.dirname(__file__)}/inputs/01.txt'

with open(path) as f:
    lines = f.readlines()
    max = []
    sum = 0
    for line in lines:
        if line != "\n":
            n = int(line)
            sum += n
        else:
            max.append(sum)
            sum = 0
    max.sort(key=int, reverse=True)
    print(max[0] + max[1] + max[2])
