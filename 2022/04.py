import os

path = f'{os.path.dirname(__file__)}/inputs/04.txt'

with open(path) as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        [first, second] = line.strip().split(',')
        [beginFirst, endFirst] = first.split('-')
        [beginSecond, endSecond] = second.split('-')
        firstRange = range(int(beginFirst), int(endFirst)+1)
        secondRange = range(int(beginSecond), int(endSecond)+1)
        intersection = list(set(firstRange) & set(secondRange))

        if len(intersection) > 0:
            sum += 1

print(sum)


# SOLUTION 1
# with open(path) as f:
#     lines = f.readlines()
#     sum = 0
#     for line in lines:
#         [first, second] = line.strip().split(',')
#         [beginFirst, endFirst] = first.split('-')
#         [beginSecond, endSecond] = second.split('-')
#         firstRange = range(int(beginFirst), int(endFirst)+1)
#         secondRange = range(int(beginSecond), int(endSecond)+1)
#         union = list(set(firstRange) | set(secondRange))

#         if len(union) <= len(firstRange) or len(union) <= len(secondRange):
#             sum += 1
