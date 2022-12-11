import os


path = f'{os.path.dirname(__file__)}/inputs/10.txt'

with open(path) as f:
    lines = f.readlines()
    count = 0
    X = 1
    for line in lines:
        Xstart = X
        if line == 'noop\n':
            count += 1
        else:
            [ope, value] = line.split()
            X += int(value)
            count += 1
            if (count - 1) == Xstart or (count - 1) == Xstart - 1 or (count - 1) == Xstart + 1:
                print('#', end='')
            else:
                print('.', end='')
            if count == 40:
                print('\n', end='')
                count = 0
            # print(count, Xstart)
            count += 1
        if (count - 1) == Xstart or (count - 1) == Xstart - 1 or (count - 1) == Xstart + 1:
            print('#', end='')
        else:
            print('.', end='')
        if count == 40:
            print('\n', end='')
            count = 0
        # print(count, Xstart)


# print(count)
# print(X)
# print(strength)


# SOLUTION 1 :
# with open(path) as f:
#     lines = f.readlines()
#     count = 0
#     X = 1
#     strength = 0
#     for line in lines:
#         Xstart = X
#         if line == 'noop\n':
#             count += 1

#         else:
#             [ope, value] = line.split()
#             X += int(value)
#             count += 1
#             if (count == 20 or count == 60 or count == 100 or count == 140 or count == 180 or count == 220):
#                 strength += Xstart * count
#             count += 1
#         if (count == 20 or count == 60 or count == 100 or count == 140 or count == 180 or count == 220):
#             strength += Xstart * count

# print(count)
# print(X)
# print(strength)
