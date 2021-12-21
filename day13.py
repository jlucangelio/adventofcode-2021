with open("day13.in") as f:
    lines = f.read().splitlines()

dots = set()

for i, line in enumerate(lines):
    if line == "":
        break

    x, y = line.split(",")
    dots.add((int(x), int(y)))

# folds

for line in lines[i+1:]:
    _, _, fold = line.split(" ")

    axis, num = fold.split("=")
    num = int(num)

    new_dots = set()
    if axis == "x":
        # vertical line at |num|.
        for (xpos, ypos) in dots:
            if xpos > num:
                newxpos = num - (xpos - num)
                new_dots.add((newxpos, ypos))
            else:
                new_dots.add((xpos, ypos))
    elif axis == "y":
        # horizontal line at |num|
        for (xpos, ypos) in dots:
            if ypos > num:
                newypos = num - (ypos - num)
                new_dots.add((xpos, newypos))
            else:
                new_dots.add((xpos, ypos))

    dots = new_dots
    print(len(new_dots))

max_x = 0
max_y = 0
for (x, y) in dots:
    max_x = max(max_x, x)
    max_y = max(max_y, y)

print(max_x, max_y)

for j in range(max_y + 1):
    print("".join(["#" if (i, j) in dots else " " for i in range(max_x + 1)]))
