import os
import pydash
import string

path = f'{os.path.dirname(__file__)}/inputs/03.txt'

with open(path) as f:
    lines = f.readlines()
    sum = 0
    chunks = pydash.chunk(lines, 3)
    for linesBy3 in chunks:
        arr = list(map(lambda x: list(x), linesBy3))
        union = pydash.intersection(*arr)
        letter = union[0]

        if letter.isupper():
            index = string.ascii_lowercase.index(letter.lower()) + 26
        else:
            index = string.ascii_lowercase.index(letter)
        sum += index + 1
    print(sum)


# SOLUTION 1:
# with open(path) as f:
#     lines = f.readlines()
#     sum = 0
#     for line in lines:
#         half = int((len(line) - 1) / 2)
#         first = line[:half]
#         second = line[half:]
#         union = pydash.intersection(list(first), list(second))
#         letter = union[0]
#         if letter.isupper():
#             index = string.ascii_lowercase.index(letter.lower()) + 26
#         else:
#             index = string.ascii_lowercase.index(letter)
#         sum += index + 1
#         print(index)
#     print(sum)
