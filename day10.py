with open("day10.in") as f:
    lines = [line.strip() for line in f.readlines()]

# lines = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
complete_points = {"(": 1, "[": 2, "{": 3, "<": 4}

score = 0
scores = []
for line in lines:
    stack = []

    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        else:
            if len(c) == 0:
                assert(False)

            opening = stack.pop()

            if opening == "(" and c != ")":
                print("corrupted, expected ) but found", c)
                score += points[c]
                break

            if opening == "[" and c != "]":
                print("corrupted, expected ] but found", c)
                score += points[c]
                break

            if opening == "{" and c != "}":
                print("corrupted, expected } but found", c)
                score += points[c]
                break

            if opening == "<" and c != ">":
                print("corrupted, expected > but found", c)
                score += points[c]
                break
    else:
        subscore = 0
        while len(stack) > 0:
            subscore = subscore * 5 + complete_points[stack.pop()]
        print(subscore)
        scores.append(subscore)


print(score)
print(sorted(scores))
print(sorted(scores)[len(sorted(scores)) // 2])
