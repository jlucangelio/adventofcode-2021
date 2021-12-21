with open("day01.in") as f:
    lines = [int(d.strip()) for d in f.readlines()]

print(sum([1 for i in range(1, len(lines)) if lines[i-1] < lines[i]]))


def sum_3(l: list, index: int):
    return sum(l[index:index+3])


print(sum([1 for i in range(0, len(lines)-3)
      if sum_3(lines, i) < sum_3(lines, i+1)]))
