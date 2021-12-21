with open("day02.in") as f:
    lines = f.readlines()

depth = 0
pos = 0

for l in lines:
    action, value = l.split()
    value = int(value)

    if action == "forward":
        pos += value
    elif action == "down":
        depth += value
    elif action == "up":
        depth -= value

print(depth * pos)


depth = 0
pos = 0
aim = 0

for l in lines:
    action, value = l.split()
    value = int(value)

    if action == "forward":
        pos += value
        depth += aim * value
    elif action == "down":
        aim += value
    elif action == "up":
        aim -= value

print(depth * pos)
