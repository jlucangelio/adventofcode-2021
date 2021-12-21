from collections import deque

INPUT = """8548335644
6576521782
1223677762
1284713113
6125654778
6435726842
5664175556
1445736556
2248473568
6451473526"""


def print_octopi(os):
    for r in os:
        print("".join([str(n) for n in r]))


class Pos(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.max_x = 9
        self.max_y = 9


    def adjacent(self):
        for i in [-1, 0, 1]:
            if self.x + i < 0 or self.x + i > self.max_x:
                continue
            for j in [-1, 0, 1]:
                if self.y + j < 0 or self.y + j > self.max_y:
                    continue
                if i == 0 and j == 0:
                    continue
                yield Pos(self.x + i, self.y + j)


    def as_tuple(self):
        return (self.x, self.y)


    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)


octopi = [[int(e) for e in line.strip()] for line in INPUT.splitlines()]

nflashes = 0
for s in range(1000):
    # print_octopi(octopi)
    # print()
    passed_9 = deque()
    added = set()
    flashed = set()

    for i in range(10):
        for j in range(10):
            level = octopi[i][j]
            octopi[i][j] = level + 1
            if level >= 9:
                passed_9.append(Pos(i, j))

    while len(passed_9) > 0:
        o = passed_9.popleft()
        # print("o", o)
        if o.as_tuple() in flashed:
            continue

        flashed.add(o.as_tuple())
        for a in o.adjacent():
            level_a = octopi[a.x][a.y]
            octopi[a.x][a.y] = level_a + 1
            if level_a >= 9 and a.as_tuple() not in added:
                passed_9.append(a)
                added.add(a.as_tuple())
                # print("a", a)

    for f in flashed:
        octopi[f[0]][f[1]] = 0

    nflashes += len(flashed)
    if s == 99:
        print(nflashes)

    if len(flashed) == 100:
        print(s + 1)
        break
