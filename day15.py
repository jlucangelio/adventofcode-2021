import heapq

with open("day15.in") as f:
    risk_level = [[int(l) for l in row] for row in f.read().splitlines()]

# print(len(risk_level), len(risk_level[0]))

# SMALL_INPUT = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581""".splitlines()
# risk_level = [[int(l) for l in row] for row in SMALL_INPUT]


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


def shortest_path(m, source):
    q = []
    # q = set()
    dist = {}
    prev = {}
    l = len(m)

    for i in range(l):
        for j in range(l):
            p = (i, j)
            # q.add(p)
            dist[p] = 9 * 2 * l + 1
            prev[p] = None

    heapq.heappush(q, (0, source))
    # dist[source] = 0

    while len(q) > 0:
        pri, u = heapq.heappop(q)
        # u = min(q, key=lambda x: dist[x])
        # q.remove(u)

        if pri <= dist[u]:
            dist[u] = pri
            for v in Pos(u[0], u[1], l - 1, l - 1).neighbors():
                vt = v.as_tuple()
                # if vt in q:
                alt = dist[u] + m[v.x][v.y]
                if alt < dist[vt]:
                    dist[vt] = alt
                    prev[vt] = u
                    heapq.heappush(q, (dist[vt], vt))

    return dist, prev


def increase_and_wrap(rl, i, j, l):
    shift = i // l + j // l
    # print(i, j, shift)
    if rl + shift > 9:
        return (rl + shift) % 10 + 1
    else:
        return rl + shift


dist, prev = shortest_path(risk_level, (0, 0))
print(dist[(99, 99)])

new_m = []
l = len(risk_level)
for i in range(5*l):
    row = [0 for _ in range(5*l)]
    for j in range(5*l):
        row[j] = increase_and_wrap(risk_level[i % l][j % l], i, j, l)

    new_m.append(row)

dist, prev = shortest_path(new_m, (0, 0))
print(dist[(l * 5 - 1, l * 5 - 1)])
