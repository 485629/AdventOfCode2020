class MemoryGame:

    def __init__(self, l):
        self.len = len(l)
        self.num = l[-1]
        self.indexes = {}
        for i in range(len(l)):
            self.indexes.setdefault(l[i], []).append(i)

    def new_game(self):
        for i in range(self.len, 2020):
            if len(self.indexes.setdefault(self.num, [])) < 2:
                if len(self.indexes.setdefault(0, [])) < 2:
                    self.num = 0
                    self.indexes[0].append(i)
                else:
                    self.num = 0
                    self.indexes[0][0] = self.indexes[0][1]
                    self.indexes[0][1] = i
            else:
                temp = self.indexes[self.num][1] - self.indexes[self.num][0]
                if len(self.indexes.setdefault(temp, [])) < 2:
                    self.indexes[temp].append(i)
                else:
                    self.indexes[temp][0] = self.indexes[temp][1]
                    self.indexes[temp][1] = i
                self.num = temp
        return self.num


with open("input.txt", "r") as f:
    l = [int(x) for x in f.read().split(",")]

print(MemoryGame(l).new_game())
