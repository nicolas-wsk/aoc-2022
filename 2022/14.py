import os
import pydash

path = f'{os.path.dirname(__file__)}/inputs/14.txt'

with open(path) as f:
    lines = f.readlines()

    lines = [[tuple(map(int, y.strip().split(','))) for y in x.strip().split('->')]
             for x in lines]
    # print(lines)
    allLines = pydash.flatten(lines)
    maxX = max(allLines, key=lambda x: x[0])[0]
    minX = min(allLines, key=lambda x: x[0])[0]
    maxY = max(allLines, key=lambda x: x[1])[1]
    # print(maxX, maxY)
    # print(allLines)
    coords = {}

    for xSand in range(minX - 1000, maxX + 1000):
        for ySand in range(maxY + 3):
            coords[(xSand, ySand)] = '.'
        coords[(xSand, maxY + 2)] = '#'

    for line in lines:
        for idx, (xNext, yNext) in enumerate(line[1:]):
            (xPrev, yPrev) = line[idx]
            if (xNext == xPrev):
                for i in range(min(yNext, yPrev), max(yNext, yPrev) + 1):
                    coords[(xNext, i)] = '#'
            elif (yNext == yPrev):
                for i in range(min(xNext, xPrev), max(xNext, xPrev) + 1):
                    coords[(i, yNext)] = '#'

    (xSand, ySand) = (500, 0)
    coords[(xSand, ySand)] = '+'
    sum = 0
    isStop = True

    while isStop:
        sum += 1

        while ySand < maxY + 2:
            if (coords[(xSand, ySand + 1)] == '.'):
                ySand += 1
            elif (coords[(xSand - 1, ySand + 1)] == '.'):
                xSand -= 1
                ySand += 1
            elif (coords[(xSand + 1, ySand + 1)] == '.'):
                xSand += 1
                ySand += 1
            else:
                coords[(xSand, ySand)] = '#'
                # print(xSand, ySand)
                if (xSand == 500 and ySand == 0):
                    isStop = False
                    break
                xSand = 500
                ySand = 0
                break

        print(sum)

# Print the map
# for y in range(maxY + 3):
#     for x in range(minX - 10, maxX + 10):
#         if x == maxX + 9:
#             print(coords[(x, y)], end='\n')
#         else:
#             print(coords[(x, y)], end='')
