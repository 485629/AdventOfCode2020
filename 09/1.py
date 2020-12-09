import itertools


class XMAS:

    def __init__(self, preamble, data):
        self.preamble = preamble
        self.data = data
        self.check()

    def check(self):
        for i in range(self.preamble, len(self.data)):
            if self.data[i] not in [a + b for [a, b] in itertools.combinations(self.data[i - 25:i], 2)]:
                print(self.data[i])
                return


l = []
with open("input.txt", "r") as f:
    for line in f:
        l.append(int(line.strip()))

x = XMAS(25, l)
