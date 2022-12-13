import os
import numpy as np
from treelib import Node, Tree


pathInput = f'{os.path.dirname(__file__)}/inputs/07.txt'


class Size(object):
    def __init__(self, size): \
        self.size = int(size)


with open(pathInput) as f:
    lines = f.readlines()
    tree = Tree()
    tree.create_node("/", "root", data=Size(0))
    path = "/"
    for line in lines[1:]:
        if line.startswith('$'):
            if line.startswith('$ cd'):
                if (line == '$ cd ..\n'):
                    path = path[:path.rfind('/')]
                else:
                    if path == '/':
                        path += line.split(' ')[2].strip()
                    else:
                        path += "/" + line.split(' ')[2].strip()
        else:
            currentDir = path[path.rfind('/') + 1:]
            if line.startswith('dir'):
                dir = line.split(' ')[1].strip()
                if currentDir == '':
                    tree.create_node(dir, '/' + dir, "root", data=Size(0))
                else:
                    tree.create_node(
                        dir, path + '/' + dir, parent=path, data=Size(0))
            else:
                size = int(line.split(' ')[0])
                newPath = path
                while newPath != '':
                    node = tree.get_node('root' if newPath == '/' else newPath)
                    if node is not None:
                        tree.update_node('root' if newPath == '/' else newPath,
                                         data=Size(int(node.data.size) + size))
                    newPath = newPath[:newPath.rfind('/')]

print(tree.show())
print(tree.show(data_property='size'))


# Full storage
sub_t = tree.children('root')

root = tree.get_node('root')
if root is not None:
    total = root.data.size
    for n in sub_t:
        print(n.data.size, sub_t)
        total += n.data.size

    print('TOTAL', total)


def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return arr[i]


# total 70000000 - 46090134 = 23909866 -> 30000000 - 23909866 = 6090134
sum = 0
test = [tree[node].data.size for node in
        tree.expand_tree(mode=Tree.DEPTH)]

print(sorted(test, key=lambda x: abs(6090134-x)))  # 6400111
