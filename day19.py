with open("day19.in") as f:
    lines = f.read().splitlines()


class Probe(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Scanner(object):
    def __init__(self, index):
        self.index = index
        self.probes = []


    def add_probe(self, probe):
        self.probes.append(probe)


scanners = {}
new_scanner = True
scanner_index = 0
for line in lines:
    if new_scanner:
        assert(len(line) > 0)
        _, _, index, _ = line.split()
        scanner_index = int(index)
        scanners[scanner_index] = Scanner(scanner_index)
        new_scanner = False
    else:
        if len(line) == 0:
            new_scanner = True
        else:
            x, y, z = line.split(",")
            x = int(x)
            y = int(y)
            z = int(z)
            scanners[scanner_index].add_probe(Probe(x, y, z))

nscanners = len(scanners)
print(nscanners)

for i in range(nscanners):
    for j in range(nscanners):
        # for each pair of probes, assume they're the same probe,
        # adjust the relative positions, and see if there are at least 12
        # overlaps.
        pass
