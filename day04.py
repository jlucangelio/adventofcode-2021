def wins(board):
    r_5 = range(5)
    for r in r_5:
        if all([board[(r, j)] for j in r_5]):
            return True

    for c in r_5:
        if all([board[(i, c)] for i in r_5]):
            return True


def sum_board(board, called):
    s = 0

    for i in range(5):
        for j in range(5):
            if not called[(i,j)]:
                s += board[i][j]

    return s


with open("day04.in") as f:
    lines = [l.strip() for l in f.readlines()]

called = [int(c) for c in lines[0].split(",")]

boards = []
nums = {}
called_by_board = []

for i in range((len(lines) - 1) // 6):
    boards.append([[int(v) for v in r.split()] for r in lines[6*i+2:6*i+7]])
    called_by_board.append({})

for bindex, board in enumerate(boards):
    for i, r in enumerate(board):
        for j, v in enumerate(r):
            if v not in nums:
                nums[v] = {}

            nums[v][bindex] = (i,j)
            called_by_board[bindex][(i,j)] = False

won = set()
for c in called:
    if c in nums:
        boards_with_num = nums[c]

        for bindex, pos in boards_with_num.items():
            if bindex in won:
                continue

            called_by_board[bindex][pos] = True

            if wins(called_by_board[bindex]):
                print(bindex)
                s = sum_board(boards[bindex], called_by_board[bindex])
                print(s * c)
                print()
                won.add(bindex)
                continue
