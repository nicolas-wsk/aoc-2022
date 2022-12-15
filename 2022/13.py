import os
import pydash
import json


def cmp_packets(left, right):
    match (left, right):
        case int(left), int(right):
            if left < right:
                return 1
            elif left > right:
                return -1
            else:
                return 0
        case int(), list():
            return cmp_packets([left], right)
        case list(), int():
            return cmp_packets(left, [right])
        case list(), list():
            for l, r in zip(left, right):
                ret = cmp_packets(l, r)
                if ret != 0:
                    return ret
            if len(right) > len(left):
                return 1
            elif len(right) < len(left):
                return -1
            else:
                return 0


path = f'{os.path.dirname(__file__)}/inputs/13.txt'

with open(path) as f:
    lines = f.readlines()

    lines = list(map(lambda x: json.loads(
        x.strip()), filter(lambda x: x != '\n', lines)))
    # print(lines)
    lines.append([[2]])
    lines.append([[6]])
    lines = pydash.sort(lines, comparator=cmp_packets, reverse=True)
    print(lines)

    divider1 = lines.index([[2]])
    divider2 = lines.index([[6]])
    sum = (divider1 + 1) * (divider2 + 1)
    print(divider1, divider2)
    print(sum)


# SOLUTION 1:
# with open(path) as f:
#     lines = f.readlines()
#     lines = pydash.chunk(lines, 3)

#     sum = []

#     for idx, line in enumerate(lines):
#         left = json.loads(line[0].strip())
#         right = json.loads(line[1].strip())

#         bool = cmp_packets(left, right)
#         print(bool)
#         if (bool == 1):
#             sum.append(idx + 1)

# print(sum)
# print(pydash.sum_(sum))
