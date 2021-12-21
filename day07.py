import math

with open("day07.in") as f:
    crabs = [int(v) for v in f.read().split(",")]

# line = "16,1,2,0,4,2,7,1,2,14"
s = sorted(crabs)

# print(s)
# print(len(s))

print(sum([abs(s[len(s)//2] - v) for v in s]))


def sum_to(n):
    return (n * (n+1)) // 2


min_cost = None
min_p = None
for p in range(2000):
    cost = 0
    for c in crabs:
        cost += sum_to(abs(p - c))

    if min_cost is None:
        min_cost = cost
        min_p = p
    else:
        if cost < min_cost:
            min_cost = cost
            min_p = p

print(min_p)
print(min_cost)
