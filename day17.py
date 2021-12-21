from collections import namedtuple

class Pos(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Vel(object):
    def __init__(self, vx: int, vy: int) -> None:
        self.vx = vx
        self.vy = vy


INPUT = "target area: x=241..273, y=-97..-63"

target = INPUT.split(":")[1].strip()

target_x, target_y = target.split(", ")

x_min, x_max = [int(v) for v in target_x.split("=")[1].split("..")]
y_min, y_max = [int(v) for v in target_y.split("=")[1].split("..")]

ta = (x_min, x_max, y_min, y_max)


def move(initial_v, nsteps, target_area):
    p = Pos(0, 0)
    v = initial_v
    success = False
    max_y = 0

    for s in range(nsteps):
        p.x += v.vx
        p.y += v.vy

        if v.vx > 0:
            v.vx -= 1
        elif v.vx < 0:
            v.vx += 1

        v.vy -= 1

        if (target_area[0] <= p.x <= target_area[1] and
            target_area[2] <= p.y <= target_area[3]):
            success = True

        max_y = max(max_y, p.y)

    return p, success, max_y


def dist_x(v):
    return (v**2 + v) // 2


def dist_for_steps(v, s):
    return s * v - ((s-1)*s) // 2


def num_steps(v, mi, ma):
    count = 0
    x = 0
    while x < mi:
        x += v
        count += 1
        v -= 1

        if v == 0:
            break

    if x < mi or x > ma:
        return None

    else:
        return count

total_successful = 0
best_y = 0
for vx in range(1, ta[1] + 1):
    if dist_x(vx) < ta[0]:
        # print("did not make it")
        # we never make it
        continue

    s = num_steps(vx, ta[0], ta[1])
    if not s:
        # print("cannot touch")
        # cannot touch the target area with this velocity
        continue

    # we can touch the target area with this velocity
    # if we move faster than the bottom of the target area, we miss it
    # in one step
    min_vy = ta[2]

    # negative vy's:
    for vy in range(min_vy, 1):
        if dist_for_steps(vy, s) < ta[2]:
            # the first step that touches in the x axis
            # results in a y axis that's too low.
            continue

        p, success, max_y = move(Vel(vx, vy), 30 * s, ta)

        if success:
            total_successful += 1
            best_y = max(max_y, best_y)

    for vy in range(1, 1000):
        p, success, max_y = move(Vel(vx, vy), 30 * s, ta)

        if success:
            total_successful += 1
            best_y = max(max_y, best_y)

print(best_y, total_successful)
