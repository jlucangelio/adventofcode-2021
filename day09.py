from collections import deque

with open("day09.in") as f:
    heightmap = [[int(d) for d in line.strip()] for line in f.readlines()]

class Pos(object):
    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y


    def neighbors(self):
        if self.x > 0:
            yield Pos(self.x - 1, self.y, self.max_x, self.max_y)
        if self.y > 0:
            yield Pos(self.x, self.y - 1, self.max_x, self.max_y)
        if self.x < self.max_x:
            yield Pos(self.x + 1, self.y, self.max_x, self.max_y)
        if self.y < self.max_y:
            yield Pos(self.x, self.y + 1, self.max_x, self.max_y)


    def as_tuple(self):
        return (self.x, self.y)


    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)


def basin_size(lp, heightmap):
    visited = set()
    next = deque([lp])

    while len(next) > 0:
        p = next.popleft()
        visited.add(p.as_tuple())

        for n in p.neighbors():
            if n.as_tuple() not in visited and heightmap[n.x][n.y] < 9:
                next.append(n)

    return len(visited)


p = Pos(1, 1, 3, 3)
for n in p.neighbors():
    print(n)

side = len(heightmap)

low_points = []
risk_sum = 0
for i in range(side):
    for j in range(side):
        p = Pos(i, j, side - 1, side - 1)
        if all([heightmap[i][j] < heightmap[n.x][n.y] for n in Pos(i, j, side - 1, side - 1).neighbors()]):
            low_points.append(p)
            risk_sum += heightmap[i][j] + 1

print(risk_sum)

sizes = []
print(len(low_points))
for lp in low_points:
    size = basin_size(lp, heightmap)
    sizes.append(size)

ss = sorted(sizes)
print(ss[-3] * ss[-2] * ss[-1])
