import os


path = f'{os.path.dirname(__file__)}/inputs/09.txt'

with open(path) as f:
    lines = f.readlines()
    head = {'x': 0, 'y': 0}
    tail = [{'x': 0, 'y': 0} for _ in range(9)]
    visited = []

    for line in lines:
        direction = line.split(' ')[0]
        value = int(line.split(' ')[1])

        for _ in range(value):
            if (direction == 'R'):
                head['x'] += 1
            if (direction == 'L'):
                head['x'] -= 1
            if (direction == 'U'):
                head['y'] += 1
            if (direction == 'D'):
                head['y'] -= 1

            for i in range(9):
                headX = head['x'] if i == 0 else tail[i - 1]['x']
                headY = head['y'] if i == 0 else tail[i - 1]['y']

                if headX == tail[i]['x'] + 2 and headY == tail[i]['y']:
                    tail[i]['x'] += 1
                if headX == tail[i]['x'] - 2 and headY == tail[i]['y']:
                    tail[i]['x'] -= 1
                if headX == tail[i]['x'] and headY == tail[i]['y'] + 2:
                    tail[i]['y'] += 1
                if headX == tail[i]['x'] and headY == tail[i]['y'] - 2:
                    tail[i]['y'] -= 1
                if headX == tail[i]['x'] + 1 and headY == tail[i]['y'] + 2:
                    tail[i]['x'] += 1
                    tail[i]['y'] += 1
                if headX == tail[i]['x'] + 1 and headY == tail[i]['y'] - 2:
                    tail[i]['x'] += 1
                    tail[i]['y'] -= 1
                if headX == tail[i]['x'] - 1 and headY == tail[i]['y'] + 2:
                    tail[i]['x'] -= 1
                    tail[i]['y'] += 1
                if headX == tail[i]['x'] - 1 and headY == tail[i]['y'] - 2:
                    tail[i]['x'] -= 1
                    tail[i]['y'] -= 1
                if headX == tail[i]['x'] + 2 and headY == tail[i]['y'] + 1:
                    tail[i]['x'] += 1
                    tail[i]['y'] += 1
                if headX == tail[i]['x'] + 2 and headY == tail[i]['y'] - 1:
                    tail[i]['x'] += 1
                    tail[i]['y'] -= 1
                if headX == tail[i]['x'] - 2 and headY == tail[i]['y'] + 1:
                    tail[i]['x'] -= 1
                    tail[i]['y'] += 1
                if headX == tail[i]['x'] - 2 and headY == tail[i]['y'] - 1:
                    tail[i]['x'] -= 1
                    tail[i]['y'] -= 1
                # additional moves
                if headX == tail[i]['x'] + 2 and headY == tail[i]['y'] + 2:
                    tail[i]['x'] += 1
                    tail[i]['y'] += 1
                if headX == tail[i]['x'] + 2 and headY == tail[i]['y'] - 2:
                    tail[i]['x'] += 1
                    tail[i]['y'] -= 1
                if headX == tail[i]['x'] - 2 and headY == tail[i]['y'] + 2:
                    tail[i]['x'] -= 1
                    tail[i]['y'] += 1
                if headX == tail[i]['x'] - 2 and headY == tail[i]['y'] - 2:
                    tail[i]['x'] -= 1
                    tail[i]['y'] -= 1

                if i == 8:
                    visited.append(f"{ tail[i]['x']}-{ tail[i]['y']}")

print(head)
print(tail)
print(visited)
print(set(visited))
print(len(set(visited)))


# with open(path) as f:
#     lines = f.readlines()
#     head = {'x': 0, 'y': 0}
#     tail = {'x': 0, 'y': 0}
#     visited = []

#     for line in lines:
#         direction = line.split(' ')[0]
#         value = int(line.split(' ')[1])

#         for _ in range(value):
#             if (direction == 'R'):
#                 head['x'] += 1
#             if (direction == 'L'):
#                 head['x'] -= 1
#             if (direction == 'U'):
#                 head['y'] += 1
#             if (direction == 'D'):
#                 head['y'] -= 1

#             if head['x'] == tail['x'] + 1 and head['y'] == tail['y']:  # right
#                 print(head)
#                 print(tail)
#             if head['x'] == tail['x'] - 1 and head['y'] == tail['y']:  # left
#                 print(head)
#                 print(tail)
#             if head['x'] == tail['x'] and head['y'] == tail['y'] + 1:  # up
#                 print(head)
#                 print(tail)
#             if head['x'] == tail['x'] and head['y'] == tail['y'] - 1:  # down
#                 print(head)
#                 print(tail)
#             if head['x'] == tail['x'] + 2 and head['y'] == tail['y']:  # right
#                 tail['x'] += 1
#             if head['x'] == tail['x'] - 2 and head['y'] == tail['y']:
#                 tail['x'] -= 1
#             if head['x'] == tail['x'] and head['y'] == tail['y'] + 2:
#                 tail['y'] += 1
#             if head['x'] == tail['x'] and head['y'] == tail['y'] - 2:
#                 tail['y'] -= 1
#             if head['x'] == tail['x'] + 1 and head['y'] == tail['y'] + 2:
#                 tail['x'] += 1
#                 tail['y'] += 1
#             if head['x'] == tail['x'] + 1 and head['y'] == tail['y'] - 2:
#                 tail['x'] += 1
#                 tail['y'] -= 1
#             if head['x'] == tail['x'] - 1 and head['y'] == tail['y'] + 2:
#                 tail['x'] -= 1
#                 tail['y'] += 1
#             if head['x'] == tail['x'] - 1 and head['y'] == tail['y'] - 2:
#                 tail['x'] -= 1
#                 tail['y'] -= 1
#             if head['x'] == tail['x'] + 2 and head['y'] == tail['y'] + 1:
#                 tail['x'] += 1
#                 tail['y'] += 1
#             if head['x'] == tail['x'] + 2 and head['y'] == tail['y'] - 1:
#                 tail['x'] += 1
#                 tail['y'] -= 1
#             if head['x'] == tail['x'] - 2 and head['y'] == tail['y'] + 1:
#                 tail['x'] -= 1
#                 tail['y'] += 1
#             if head['x'] == tail['x'] - 2 and head['y'] == tail['y'] - 1:
#                 tail['x'] -= 1
#                 tail['y'] -= 1

#             visited.append(f"{tail['x']}-{tail['y']}")

#             print(head)
#             print(tail)

#         print(head)
#         print(tail)

# print(head)
# print(tail)
# print(visited)
# print(set(visited))
# print(len(set(visited)))
