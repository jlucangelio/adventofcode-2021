from collections import defaultdict

class Pixel(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def neighbors(self):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                yield (self.x + i, self.y + j)


    def num(self, image):
        bin_str = []
        for n in self.neighbors():
            # print("neighbor", n)
            bin_str.append("1" if image[n] == "#" else "0")

        return int("".join(bin_str), base=2)


    def __str__(self):
        return self.val


def print_image(img, lower, upper):
    to_print = []
    for i in range(lower, upper):
        row = []
        for j in range(lower, upper):
            row.append(img[(i, j)])
        to_print.append("".join(row))

    print("\n".join(to_print))


# with open("day20.small.in") as f:
with open("day20.in") as f:
    lines = f.read().splitlines()

algo = [c for c in lines[0]]
assert(len(algo) == 512)

side = len(lines)
image = defaultdict(lambda: ".")
for i, l in enumerate(lines[2:]):
    for j, c in enumerate(l):
        image[(i,j)] = c

for s in range(1, 50 + 1):
    if s % 2 == 1:
        new_image = defaultdict(lambda: "#")
    else:
        new_image = defaultdict(lambda: ".")
    count = 0
    for i in range(-s, side + s):
        for j in range(-s, side + s):
            p = Pixel(i, j)
            n = p.num(image)
            val = algo[n]
            new_image[(i, j)] = val
            if val == "#":
                count += 1
    print("step", s, "count", count)
    image = new_image
