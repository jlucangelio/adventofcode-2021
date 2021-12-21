import copy
import time

class Pair(object):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


    def mag(self):
        return 3 * self.lhs.mag() + 2 * self.rhs.mag()


    def __str__(self):
        return "[" + str(self.lhs) + "," + str(self.rhs) + "]"


class RegularNumber(object):
    def __init__(self, v):
        self.v = v


    def mag(self):
        return self.v


    def __str__(self):
        return str(self.v)


def parse_pair(s: str):
    # [[0,6],[[[4,0],[6,6]],[[2,2],9]]]

    # pair -> "[" element "," element "]"
    # element -> literal | pair

    assert(s[0] == "[")
    assert(s[-1] == "]")

    substr = s[1:-1]

    # find the comma
    bracket_count = 0
    comma_index = 0
    for i, c in enumerate(substr):
        if c == "[":
            bracket_count += 1
        elif c == "]":
            bracket_count -= 1
        elif c == ",":
            if bracket_count == 0:
                comma_index = i
                break

    l = substr[:comma_index]
    r = substr[comma_index + 1:]

    return Pair(parse_element(l), parse_element(r))


def parse_element(e):
    if e[0] == "[":
        return parse_pair(e)
    else:
        return RegularNumber(int(e))


def add(n1, n2):
    return reduce(Pair(n1, n2))


def reduce(n):
    attempt_reduce = True

    while attempt_reduce:
        could, l, r, new_n = explode(n)
        if could:
            n = new_n
            continue

        could, new_n = split(n)
        if could:
            n = new_n
            continue

        n = new_n
        attempt_reduce = False

    return n


def add_to_leftmost(n, val):
    if isinstance(n, RegularNumber):
        n.v += val
    else:
        # |n| is a pair
        add_to_leftmost(n.lhs, val)


def add_to_rightmost(n, val):
    if isinstance(n, RegularNumber):
        n.v += val
    else:
        # |n| is a pair
        add_to_rightmost(n.rhs, val)


def explode(n, nesting=0):
    if isinstance(n, RegularNumber):
        # print("explode RN")
        return False, None, None, n

    assert(nesting <= 4)

    # |n| is a pair
    if nesting == 4:
        assert(isinstance(n.lhs, RegularNumber))
        assert(isinstance(n.rhs, RegularNumber))
        return True, n.lhs.v, n.rhs.v, RegularNumber(0)

    # |nesting| < 4
    exploded, l, r, new_lhs = explode(n.lhs, nesting + 1)
    if exploded:
        if r:
            add_to_leftmost(n.rhs, r)
        n.lhs = new_lhs
        return True, l, None, n

    exploded, l, r, new_rhs = explode(n.rhs, nesting + 1)
    if exploded:
        if l:
            add_to_rightmost(n.lhs, l)
        n.rhs = new_rhs
        return True, None, r, n

    return False, None, None, n


def split(n):
    if isinstance(n, RegularNumber):
        if n.v > 9:
            new_lhs = RegularNumber(n.v // 2)
            new_rhs = RegularNumber(n.v // 2)
            new_rhs.v += n.v % 2
            return True, Pair(new_lhs, new_rhs)
        else:
            return False, n

    # it's a pair
    success, new_lhs = split(n.lhs)
    if success:
        n.lhs = new_lhs
        return True, n

    success, new_rhs = split(n.rhs)
    if success:
        n.rhs = new_rhs
    return success, n


with open("day18.in") as f:
    INPUT = f.read().splitlines()

numbers = [parse_pair(l) for l in INPUT]

res = numbers[0]
for l in numbers[1:]:
    res = add(res, l)

print(res)
print(res.mag())

max_mag = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            # before = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            res = add(parse_pair(INPUT[i]), parse_pair(INPUT[j]))
            # after = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            max_mag = max(max_mag, res.mag())

            if res.mag() == max_mag:
                print(i, j, res)

print(max_mag)
