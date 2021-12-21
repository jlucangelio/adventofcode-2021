with open("day03.in") as f:
    lines = [l.strip() for l in f.readlines()]

counts = [0 for _ in range(len(lines[0].strip()))]

print(counts)

for line in lines:
    for i, b in enumerate(line.strip()):
        counts[i] += 1 if b == "1" else 0

print(counts)

g = []
e = []

for c in counts:
    g.append("1" if c > len(lines) / 2 else "0")
    e.append("0" if c > len(lines) / 2 else "1")

# print(g)
# print(e)
gn = int("".join(g), 2)
en = int("".join(e), 2)
print(gn * en)


def count_and_filter(ls, index, most=False):
    length = len(ls)

    if length == 1:
        return ls

    count = 0
    for l in ls:
        count += 1 if l[index] == "1" else 0

    keep = None
    if most:
        if length - count <= count:
            # There are half or more ones, keep the ones.
            keep = "1"
        else:
            # length - count > count
            # There are more zeroes, keep the zeroes.
            keep = "0"
    else:
        # most == False
        if length - count < count:
            # There are more ones, keep the zeroes.
            keep = "0"
        elif length - count > count:
            # There are more zeroes, keep the ones.
            keep = "1"
        else:
            # Same number, keep the zeroes.
            keep = "0"

    res = []
    for l in ls:
        if l[index] == keep:
            res.append(l)

    return res


o = lines
c = lines
for i in range(len(lines[0])):
    o = count_and_filter(o, i, most=True)
    c = count_and_filter(c, i, most=False)

print(o)
print(c)
on = int("".join(o), 2)
cn = int("".join(c), 2)
print(on * cn)
