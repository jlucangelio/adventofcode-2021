with open("day08.in") as f:
# with open("day08.small.in") as f:
    lines = [line.strip() for line in f.readlines()]


def segments_to_num(signal, mapping):
    if len(signal) == 2:
        return "1"
    elif len(signal) == 3:
        return "7"
    elif len(signal) == 4:
        return "4"
    elif len(signal) == 7:
        return "8"

    mapped = set([mapping[s] for s in signal])

    if len(mapped) == 5:
        if set("ce") < mapped:
            return "2"
        elif set("cf") < mapped:
            return "3"
        else:
            return "5"
    elif len(mapped) == 6:
        if "d" in mapped:
            return "6" if "e" in mapped else "9"
        else:
            return "0"


count = 0
for line in lines:
    _, displays = line.split(" | ")

    for d in displays.split(" "):
        # print(d, len(d))
        if len(d) in set([2, 3, 4, 7]):
            count += 1

print(count)

count = 0
for line in lines:
    # print(line)
    signals, displays = line.split(" | ")

    signals_to_segments = {}
    segments_to_signals = {}
    d_s = {}
    for s in signals.split(" "):
        if len(s) not in d_s:
            d_s[len(s)] = []
        d_s[len(s)].append(set(s))

    #   0:      1:      2:      3:      4:
    # aaaa    ....    aaaa    aaaa    ....
    # b    c  .    c  .    c  .    c  b    c
    # b    c  .    c  .    c  .    c  b    c
    # ....    ....    dddd    dddd    dddd
    # e    f  .    f  e    .  .    f  .    f
    # e    f  .    f  e    .  .    f  .    f
    # gggg    ....    gggg    gggg    ....

    # 5:      6:      7:      8:      9:
    # aaaa    aaaa    aaaa    aaaa    aaaa
    # b    .  b    .  .    c  b    c  b    c
    # b    .  b    .  .    c  b    c  b    c
    # dddd    dddd    ....    dddd    dddd
    # .    f  e    f  .    f  e    f  .    f
    # .    f  e    f  .    f  e    f  .    f
    # gggg    gggg    ....    gggg    gggg

    segments_to_signals["a"] = (d_s[3][0] - d_s[2][0]).pop()

    d = (d_s[5][0] & d_s[5][1] & d_s[5][2] & d_s[4][0]).pop()
    segments_to_signals["d"] = d

    segments_to_signals["b"] = (d_s[4][0] - d_s[2][0] - set([segments_to_signals["d"]])).pop()

    segments_to_signals["g"] = ((d_s[6][0] & d_s[6][1] & d_s[6][2]) - d_s[4][0] - d_s[3][0]).pop()

    segments_to_signals["e"] = (d_s[7][0] - d_s[3][0] - d_s[4][0] - set([segments_to_signals["g"]])).pop()

    adgbe = set([segments_to_signals["a"], segments_to_signals["d"],
               segments_to_signals["g"], segments_to_signals["b"],
               segments_to_signals["e"]])
    s60 = d_s[6][0] - adgbe
    s61 = d_s[6][1] - adgbe
    s62 = d_s[6][2] - adgbe

    segments_to_signals["f"] = (s60 & s61 & s62).pop()
    segments_to_signals["c"] = (d_s[2][0] - set([segments_to_signals["f"]])).pop()

    # print(segments_to_signals)
    signals_to_segments = dict([(v, k) for k, v in segments_to_signals.items()])

    n = int("".join([segments_to_num(s, signals_to_segments) for s in displays.split(" ")]))
    count += n

print(count)
