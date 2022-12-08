import os
import pydash


path = f'{os.path.dirname(__file__)}/inputs/06.txt'

with open(path) as f:
    [line] = f.readlines()
    arr = [*line]

    for idx, char in enumerate(arr):
        if idx > 12:
            # print(idx, char)

            temp = arr[idx - 13:idx]
            # print(temp, char)
            if char not in temp and pydash.uniq(temp) == temp:
                print(idx + 1)
                break


# SOLUTION 1:
# with open(path) as f:
#     [line] = f.readlines()
#     arr = [*line]

#     for idx, char in enumerate(arr):
#         if idx > 2:
#             # print(idx, char)

#             temp = arr[idx - 3:idx]
#             # print(temp, char)
#             if char not in temp and pydash.uniq(temp) == temp:
#                 print(idx + 1)
#                 break
