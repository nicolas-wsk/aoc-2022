import os


path = f'{os.path.dirname(__file__)}/inputs/08.txt'

with open(path) as f:
    [line] = f.readlines()
