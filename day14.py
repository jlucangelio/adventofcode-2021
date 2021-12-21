with open("day14.in") as f:
    lines = f.read().splitlines()

template = lines[0]
npairs = {}
for i in range(0, len(template) - 1):
    p = template[i:i + 2]
    first = i == 0
    last = i == len(template) - 2

    if p not in npairs:
        npairs[p] = [0, first, last]

    npairs[p][0] += 1

replacements = {}
for l in lines[2:]:
    match, replacement = l.split(" -> ")
    replacements[match] = replacement

for step in range(40):
    new_npairs = {}
    for p, v in npairs.items():
        r = replacements[p]
        p0 = p[0] + r
        p1 = r + p[1]
        n, first, last = v

        if p0 not in new_npairs:
            new_npairs[p0] = [0, first, False]

        new_npairs[p0][0] += n

        if p1 not in new_npairs:
            new_npairs[p1] = [0, False, last]

        new_npairs[p1][0] += n

    npairs = new_npairs

counts = {}
for p, v in npairs.items():
    n, f, l = v

    for e in p:
        if e not in counts:
            counts[e] = 0

    if f:
        counts[p[0]] += n

    counts[p[1]] += n

print(max(counts.values()) - min(counts.values()))
