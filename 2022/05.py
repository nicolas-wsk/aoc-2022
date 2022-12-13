import os

path = f'{os.path.dirname(__file__)}/inputs/05.txt'

with open(path) as f:
    lines = f.readlines()
    [structure, orders] = "".join(lines).split("\n\n")
    structureLines = structure.split("\n")
    structureLines.reverse()

    stacks = [[] for _ in range(len(structureLines))]
    for idx, line in enumerate(structureLines[0]):
        if (line.isdigit()):
            index = int(line) - 1
            for line in structureLines[1:]:
                current = line[idx]
                if current.isalpha():
                    stacks[index].append(current)
    for order in orders.split("\n"):
        [nbrCrate, fromCrate, toCrate] = [
            int(s) for s in order.split() if s.isdigit()]
        change = [stacks[fromCrate - 1].pop() for _ in range(nbrCrate)]
        change.reverse()
        for i in change:
            stacks[toCrate - 1].append(i)


result = []
for st in stacks:
    result.append(st[-1])

print("".join(result))


# SOLUTION 1:

# with open(path) as f:
#     lines = f.readlines()
#     [structure, orders] = "".join(lines).split("\n\n")
#     structureLines = structure.split("\n")
#     structureLines.reverse()
#     # print(structureLines)
#     stacks = [[] for _ in range(len(structureLines))]
#     for idx, line in enumerate(structureLines[0]):
#         if (line.isdigit()):
#             # print(line, idx)
#             index = int(line) - 1
#             for line in structureLines[1:]:
#                 current = line[idx]
#                 if current.isalpha():
#                     stacks[index].append(current)
#     for order in orders.split("\n"):
#         [nbrCrate, fromCrate, toCrate] = [
#             int(s) for s in order.split() if s.isdigit()]
#         # print(stacks)
#         change = [stacks[fromCrate - 1].pop() for _ in range(nbrCrate)]
#         # print(change)
#         for i in change:
#             stacks[toCrate - 1].append(i)
#         # print(nbrCrate, fromCrate, toCrate)

# # print(stacks)
# result = []
# for st in stacks:
#     result.append(st[-1])
# print("".join(result))
