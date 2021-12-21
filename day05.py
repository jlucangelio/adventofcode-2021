with open("day05.in") as f:
    lines = [l.strip() for l in f.readlines()]

# lines = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""".splitlines()

class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)


    def is_h_or_v(self):
        return self.x1 == self.x2 or self.y1 == self.y2


    def fill_hv(self, intersections):
        bx = self.x1 if self.x1 < self.x2 else self.x2
        ex = self.x2 if self.x1 < self.x2 else self.x1
        rangex = range(bx, ex + 1)

        by = self.y1 if self.y1 < self.y2 else self.y2
        ey = self.y2 if self.y1 < self.y2 else self.y1
        rangey = range(by, ey + 1)

        for i in rangex:
            for j in rangey:
                p = (i, j)
                if p not in intersections:
                    intersections[p] = 0

                intersections[p] += 1


    def fill_d(self, intersections):
        if self.x1 < self.x2:
            rangex = range(self.x1, self.x2 + 1)
        else:
            rangex = range(self.x1, self.x2 - 1, -1)

        if self.y1 < self.y2:
            rangey = range(self.y1, self.y2 + 1)
        else:
            rangey = range(self.y1, self.y2 - 1, -1)

        for step in range(len(rangex)):
            p = (rangex[step], rangey[step])
            if p not in intersections:
                intersections[p] = 0

            intersections[p] += 1


intersections = {}
line_objects = []
for line in lines:
    # 504,179 -> 77,179
    p1, p2 = line.split(" -> ")
    x1, y1 = p1.split(",")
    x2, y2 = p2.split(",")

    l = Line(x1, y1, x2, y2)
    line_objects.append(l)

    if l.is_h_or_v():
        l.fill_hv(intersections)

print(sum([1 for v in intersections.values() if v >= 2]))

for l in line_objects:
    if not l.is_h_or_v():
        l.fill_d(intersections)

# for j in range(10):
#     print("".join([str(intersections[(i,j)]) if (i,j) in intersections else "." for i in range(10)]))

print(sum([1 for v in intersections.values() if v >= 2]))
