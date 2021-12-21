INPUT = """QR-da
QR-end
QR-al
start-op
zh-iw
zh-start
da-PF
op-bj
iw-QR
end-HR
bj-PF
da-LY
op-PF
bj-iw
end-da
bj-zh
HR-iw
zh-op
zh-PF
HR-bj
start-PF
HR-da
QR-bj""".splitlines()

adjacent = {}

for line in INPUT:
    b, e = line.split("-")

    if b not in adjacent:
        adjacent[b] = []
    adjacent[b].append(e)

    if e not in adjacent:
        adjacent[e] = []
    adjacent[e].append(b)

print(adjacent)


def count_paths(adjacent, current, counted, bonus=None):
    adjacent_caves = adjacent[current[-1]]

    for cave in adjacent_caves:
        if cave == "start":
            continue

        if cave == "end":
            counted.add(tuple(current + [cave]))
            continue

        if cave.islower():
            # Small cave, can only visit once, except if it's the |bonus| cave.
            nvisits = current.count(cave)
            if nvisits == 0 or (cave == bonus and nvisits == 1):
                count_paths(adjacent, current + [cave], counted, bonus)

        elif cave.isupper():
            # Big cave, can visit more than once.
            count_paths(adjacent, current + [cave], counted, bonus)


counted = set()
current = ["start"]
count_paths(adjacent, current, counted)
print(len(counted))

counted = set()
for c in adjacent.keys():
    if c.islower() and c != "start" and c != "end":
        count_paths(adjacent, ["start"], counted, c)

print(len(counted))
