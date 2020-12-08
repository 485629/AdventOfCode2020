from copy import deepcopy


class HandheldGameConsole:

    def __init__(self, data):
        self.data = data
        self.copiedData = deepcopy(self.data)
        self.acc = 0
        self.s = set()
        self.index = 0

    def reset(self):
        self.data = deepcopy(self.copiedData)
        self.acc = 0
        self.s = set()
        self.index = 0

    def change(self):
        for i in range(len(self.data)):
            if self.data[i][0] == "jmp":
                self.data[i][0] = "nop"
                self.run()
                self.reset()
        for j in range(len(self.data)):
            if self.data[j][0] == "nop":
                self.data[j][0] = "jmp"
                self.run()
                self.reset()

    def run(self):
        while self.index not in self.s:
            if self.index >= len(self.data):
                print(self.acc)
                return self.acc
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

print(HandheldGameConsole(l).change())
