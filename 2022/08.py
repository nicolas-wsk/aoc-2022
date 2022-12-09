import os


path = f'{os.path.dirname(__file__)}/inputs/08.txt'

with open(path) as f:
    lines = f.readlines()
    size = len(lines)
    total = (size - 1) * 4
    arr = [[] for _ in range(size)]

    # create a 2d array
    for idx, line in enumerate(lines):
        arr[idx] = [*line.strip('\n')]
    print(arr)
    print(arr[1][4])
    total = []

    for idx_v, line in enumerate(lines[1:size-1]):
        # print(idx, line)
        for idx_h, char in enumerate(line[1: len(line) - 2]):
            isVisible = [0, 0, 0, 0]

            for idx in range(0, idx_v + 1):
                up = arr[idx_v - idx][idx_h + 1]
                # print(char, up, isVisible
                isVisible[0] += 1
                if char <= up:
                    break

            for idx in range(0, idx_h + 1):
                left = arr[idx_v + 1][idx_h - idx]
                print(char, left)
                isVisible[1] += 1

                if char <= left:
                    break

            for idx in reversed(range(idx_h + 1, size - 1)):
                right = arr[idx_v + 1][idx_h + (size - idx)]
                print(char, right)
                isVisible[2] += 1

                if char <= right:
                    break

            for idx in reversed(range(idx_v + 1, size - 1)):
                down = arr[idx_v + (size - idx)][idx_h + 1]
                print(char, down)
                isVisible[3] += 1

                if char <= down:
                    break

            total.append(isVisible[0] * isVisible[1] *
                         isVisible[2] * isVisible[3])

            print(char, isVisible)

# print(total)
print(max(total))


# SOLUTION 1:
# with open(path) as f:
#     lines = f.readlines()
#     size = len(lines)
#     total = (size - 1) * 4
#     arr = [[] for _ in range(size)]

#     # create a 2d array
#     for idx, line in enumerate(lines):
#         arr[idx] = [*line.strip('\n')]
#     print(arr)
#     print(arr[1][4])

#     for idx_v, line in enumerate(lines[1:size-1]):
#         # print(idx, line)
#         for idx_h, char in enumerate(line[1: len(line) - 2]):
#             isVisible = [True, True, True, True]

#             for idx in range(0, idx_v + 1):
#                 up = arr[idx_v - idx][idx_h + 1]
#                 # print(char, up, isVisible)
#                 if char <= up:
#                     isVisible[0] = False

#             for idx in range(0, idx_h + 1):
#                 left = arr[idx_v + 1][idx_h - idx]
#                 # print(char, left, isVisible)
#                 if char <= left:
#                     isVisible[1] = False

#             for idx in range(idx_h + 1, size - 1):
#                 right = arr[idx_v + 1][idx_h + (size - idx)]
#                 # print(char, right, isVisible)
#                 if char <= right:
#                     isVisible[2] = False
#             for idx in range(idx_v + 1, size - 1):
#                 down = arr[idx_v + (size - idx)][idx_h + 1]
#                 if char <= down:
#                     isVisible[3] = False

#             if True in isVisible:
#                 total += 1
#             # print(char, isVisible)

# print(total)
