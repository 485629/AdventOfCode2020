class MemoryGame:

    def __init__(self, l):
        self.len = len(l)
        self.num = l[-1]
        self.indexes = {}
        for i in range(len(l)):
            self.indexes.setdefault(l[i], (i,))
        self.indexes.setdefault(0, ())

    def new_game(self):
        for i in range(self.len, 30000000):
            if self.num in self.indexes.keys():
                if len(self.indexes[self.num]) < 2:
                    if len(self.indexes[0]) == 1:
                        self.num = 0
                        self.indexes[0] = (self.indexes[0][0], i)
                    elif len(self.indexes[0]) == 0:
                        self.num = 0
                        self.indexes[0] = (i, )
                    else:
                        self.num = 0
                        self.indexes[0] = (self.indexes[0][1], i)
                    continue
            temp = self.indexes[self.num][1] - self.indexes[self.num][0]
            if temp in self.indexes.keys():
                if len(self.indexes[temp]) == 1:
                    self.indexes[temp] = (self.indexes[temp][0], i)
                else:
                    self.indexes[temp] = (self.indexes[temp][1], i)
            else:
                self.indexes[temp] = (i,)
            self.num = temp
        return self.num


with open("input.txt", "r") as f:
    l = [int(x) for x in f.read().split(",")]

print(MemoryGame(l).new_game())
