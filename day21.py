from collections import namedtuple

Universe = namedtuple("Universe", "p1_pos p1_score p2_pos p2_score")

P1 = 8
P2 = 6

# P1 = 4
# P2 = 8

def deterministic_die():
    i = 0
    while True:
        yield i + 1
        i = (i + 1) % 100


# Track pos as pos - 1 to make mod easier.
p1_pos = P1 - 1
p2_pos = P2 - 1
p1_score = 0
p2_score = 0
rolls = 0

d = deterministic_die()
while (p1_score < 1000 and p2_score < 1000):
    p1_rolls = [next(d), next(d), next(d)]
    rolls += 3
    p1_move = sum(p1_rolls)

    p1_pos = (p1_pos + p1_move) % 10

    p1_score += p1_pos + 1

    if p1_score >= 1000:
        break

    p2_rolls = [next(d), next(d), next(d)]
    rolls += 3
    p2_move = sum(p2_rolls)

    p2_pos = (p2_pos + p2_move) % 10

    p2_score += p2_pos + 1

print(p1_score, p2_score, rolls)
print(min(p1_score, p2_score) * rolls)
print()

sums = {}
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            s = i + j + k
            if s not in sums:
                sums[s] = 0
            sums[s] += 1

print(sums, len(sums))


def done(universe_count):
    for u in universe_count:
        if u.p1_score < 21 and u.p2_score < 21:
            return False

    return True


nuniverses = {}
nuniverses[Universe(P1 - 1, 0, P2 - 1, 0)] = 1
while not done(nuniverses):
    # print()
    # print(len(nuniverses))
    print(len(nuniverses), sum(nuniverses.values()))
    # print(nuniverses)
    new_universes = {}
    for u, count in nuniverses.items():
        # print(u, count)
        # p1_pos p1_score p2_pos p2_score
        p1_pos, p1_score, p2_pos, p2_score = u

        if p1_score >= 21 or p2_score >= 21:
            # if the game has ended just bring that universe count forward
            if u not in new_universes:
                new_universes[u] = 0
            new_universes[u] += count
            continue

        # otherwise, have p1 play.
        for s, p1_freq in sums.items():
            # dice score |s| happens |freq| times if you roll three times.
            new_p1_pos = (p1_pos + s) % 10
            new_p1_score = p1_score + new_p1_pos + 1

            # However many universes we had before, no matter whether p1 wins
            # or not, we have more now, because we rolled the die.
            after_p1_count = count * p1_freq

            if new_p1_score >= 21:
                u = Universe(new_p1_pos, new_p1_score, p2_pos, p2_score)
                if u not in new_universes:
                    new_universes[u] = 0
                new_universes[u] += after_p1_count
                continue

            # p1 hasn't won yet, p2 gets to play
            for s, p2_freq in sums.items():
                # dice score |s| happens |freq| times if you roll three times.
                new_p2_pos = (p2_pos + s) % 10
                new_p2_score = p2_score + new_p2_pos + 1

                after_p2_count = after_p1_count * p2_freq

                u = Universe(new_p1_pos, new_p1_score, new_p2_pos, new_p2_score)
                if u not in new_universes:
                    new_universes[u] = 0
                new_universes[u] += after_p2_count


    nuniverses = new_universes

p1_wins = 0
p2_wins = 0
for u, count in nuniverses.items():
    p1_pos, p1_score, p2_pos, p2_score = u
    assert(p1_score >= 21 or p2_score >= 21)
    assert(p1_score < 21 or p2_score < 21)
    if p1_score >= 21:
        p1_wins += count
    elif p2_score >= 21:
        p2_wins += count

assert(p1_wins + p2_wins == sum(nuniverses.values()))
print(p1_wins, p2_wins, p1_wins > p2_wins)

# 444356092776315
# 268221480320175