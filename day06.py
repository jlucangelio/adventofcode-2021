with open("day06.in") as f:
    lines = f.readlines()

line = lines[0].strip()
# line = "3,4,3,1,2"

def indexof(zero_index, state, nstates):
    return (zero_index + state) % nstates


class BirdState(object):
    def __init__(self):
        self.zero_to_six = [0 for _ in range(7)]
        self.seven = 0
        self.eight = 0

        self.zero_index = 0


    def add(self, state):
        if state <= 6:
            self.zero_to_six[state] += 1
        elif state == 7:
            self.seven += 1
        elif state == 8:
            self.eight += 1

    def advance(self, days):
        for _ in range(days):
            old_seven = self.seven
            self.seven = self.eight

            # All fish in state 0 spawn fish in state 8,
            # and transition to state 6.
            self.eight = self.zero_to_six[self.zero_index]

            # 1->0, 2->1, 3->2, 4->3, 5->4, 6->5, 0->6
            self.zero_index = (self.zero_index + 1) % 7
            # All fish in state 7 transition to state 6.
            self.zero_to_six[(self.zero_index + 6) % 7] += old_seven


    def count(self):
        return sum(self.zero_to_six) + self.seven + self.eight


bs = BirdState()
for b in line.split(","):
    bs.add(int(b))

print(bs.count())

bs.advance(256)
print(bs.count())