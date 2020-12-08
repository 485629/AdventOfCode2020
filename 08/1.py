class HandheldGameConsole:

    def __init__(self, data):
        self.data = data
        self.acc = 0
        self.s = set()
        self.index = 0

    def run(self):
        while self.index not in self.s:
            if self.data[self.index][0] == "acc":
                self.acc += int(self.data[self.index][1])
                self.s.add(self.index)
                self.index += 1
            elif self.data[self.index][0] == "jmp":
                self.s.add(self.index)
                self.index += int(self.data[self.index][1])
            else:
                self.s.add(self.index)
                self.index += 1
        return self.acc


with open("input.txt", "r") as f:
    l = f.read().split("\n")
    l = [x.split() for x in l]

print(HandheldGameConsole(l).run())
