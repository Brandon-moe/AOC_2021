#https://adventofcode.com/2021/day/16
from operator import add, mul, gt, lt, eq
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().strip()
    bits = ((int(c, 16) >> i) & 1 for c in data for i in range(3, -1, -1))
    ops = add, mul, lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq
    pos = ver = 0
    def read(size):
        nonlocal pos
        pos += size
        return sum(next(bits) << i for i in range(size - 1, -1, -1))
    def packet():
        nonlocal ver
        ver += read(3)
        if (type_id := read(3)) == 4:
            go, total = read(1), read(4)
            while go:
                go, total = read(1), total << 4 | read(4)
        elif read(1) == 0:
            length = read(15) + pos
            total = packet()
            while pos < length:
                total = ops[type_id](total, packet())
        else:
            count = read(11)
            total = packet()
            for _ in range(count - 1):
                total = ops[type_id](total, packet())
        return total
    total = packet()
    return ver, total
