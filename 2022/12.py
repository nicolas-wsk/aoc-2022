import os
import string
import networkx as nx
import matplotlib.pyplot as plt


path = f'{os.path.dirname(__file__)}/inputs/12.txt'

G = nx.DiGraph()

entry = []
sum = []
with open(path) as f:
    lines = f.readlines()
    arr = [[] for _ in range(len(lines))]
    print(arr)
    for y, line in enumerate(lines):
        arr[y] = [0 for _ in range(len(line.strip()))]
        for x, char in enumerate([*line.strip()]):
            weight = string.ascii_lowercase.index(char)
            arr[y][x] = weight
    for y, line in enumerate(lines):
        for x, char in enumerate([*line.strip()]):
            weight = arr[y][x]
            if (weight == 0):
                entry.append((x, y))

            if x < len(line.strip()) - 1 and arr[y][x + 1] <= weight + 1:
                G.add_edge((x, y), (x + 1, y))
            if x > 0 and arr[y][x - 1] <= weight + 1:
                G.add_edge((x, y), (x - 1, y))
            if y < len(lines) - 1 and arr[y + 1][x] <= weight + 1:
                G.add_edge((x, y), (x, y + 1))
            if y > 0 and arr[y - 1][x] <= weight + 1:
                G.add_edge((x, y), (x, y - 1))


# nx.draw(G, with_labels=True, )
# plt.savefig("path.png")


print(entry)
for i in entry:
    try:
        path = nx.shortest_path(G, source=i, target=(88, 20))
        sum.append(len(path) - 1)
    except nx.NetworkXNoPath:
        pass

print(min(sum))
