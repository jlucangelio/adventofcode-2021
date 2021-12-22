from copy import copy
from collections import defaultdict, namedtuple

with open("day22.in") as f:
# with open("day22.small.in") as f:
    lines = f.read().splitlines()

reactor = defaultdict(bool)
for line in lines[:20]:
    # on x=0..45,y=-21..27,z=-28..20
    # print(line)

    switch, coords = line.split()

    x, y, z = coords.split(",")
    xmin, xmax = [int(v) for v in x.split("=")[1].split("..")]
    ymin, ymax = [int(v) for v in y.split("=")[1].split("..")]
    zmin, zmax = [int(v) for v in z.split("=")[1].split("..")]

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                reactor[(x, y, z)] = True if switch == "on" else False

print(sum([1 if v else 0 for v in reactor.values()]))

class Range(object):
    def __init__(self, rmin, rmax):
        self.rmin = rmin
        self.rmax = rmax


    def span(self):
        return abs(self.rmax - self.rmin + 1)


    def contains(self, block):
        return self.rmin <= block <= self.rmax


    def overlaps(self, other):
        return self.contains(other.rmin) or self.contains(other.rmax)


    def includes(self, other):
        return self.contains(other.rmin) and self.contains(other.rmax)


    def intersection(self, other):
        if self.includes(other):
            return other

        if other.includes(self):
            return self

        if not self.overlaps(other):
            return None

        if self.contains(other.rmin) and self.contains(other.rmax):
            return Range(other.rmin, other.rmax)
        elif self.contains(other.rmin):
            return Range(other.rmin, self.rmax)
        elif self.contains(other.rmax):
            return Range(self.rmin, other.rmax)


    def __str__(self):
        return "%d..%d" % (self.rmin, self.rmax)


class Cuboid(object):
    def __init__(self, xrange, yrange, zrange, on):
        self.xrange = xrange
        self.yrange = yrange
        self.zrange = zrange
        self.on = on
        self.exclusions = []


    def volume(self):
        return self.xrange.span() * self.yrange.span() * self.zrange.span()


    def exclusive_volume(self):
        return (self.xrange.span() * self.yrange.span() * self.zrange.span() -
                sum([e.exclusive_volume() for e in self.exclusions]))


    def contains(self, other):
        return all([self.xrange.includes(other.xrange),
                    self.yrange.includes(other.yrange),
                    self.zrange.includes(other.zrange)])


    def intersect(self, other):
        xint = self.xrange.intersection(other.xrange)
        yint = self.yrange.intersection(other.yrange)
        zint = self.zrange.intersection(other.zrange)

        if all([intersection is not None for intersection in [xint, yint, zint]]):
            overlap = Cuboid(xint, yint, zint, other.on)
            return overlap
        else:
            return None


    def exclude(self, other):
        overlap = self.intersect(other)
        if not overlap:
            return
        for e in self.exclusions:
            e.exclude(overlap)
        self.exclusions.append(overlap)
        return overlap


    def num_on(self):
        return self.exclusive_volume() if self.on else 0


    def __str__(self):
        return "Cuboid(x=%s,y=%s,z=%s,%s)" % (self.xrange, self.yrange, self.zrange, self.on)


original_cubes = []

for line in lines:
    # on x=0..45,y=-21..27,z=-28..20
    # print(line)

    switch, coords = line.split()
    x, y, z = coords.split(",")
    xmin, xmax = [int(v) for v in x.split("=")[1].split("..")]
    ymin, ymax = [int(v) for v in y.split("=")[1].split("..")]
    zmin, zmax = [int(v) for v in z.split("=")[1].split("..")]

    c = Cuboid(Range(xmin, xmax), Range(ymin, ymax), Range(zmin, zmax), switch == "on")
    original_cubes.append(c)

for i, ic in enumerate(original_cubes):
    for j, jc in enumerate(original_cubes):
        if i < j:
            original_cubes[i].exclude(original_cubes[j])

print(sum([c.num_on() for c in original_cubes]))
