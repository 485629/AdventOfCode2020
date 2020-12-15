class Docking:

    def __init__(self, data):
        self.data = data
        self.mask = ""
        self.values = ""
        self.results = {}
        self.compute()
        print(self.sum())

    def compute(self):
        for line in self.data:
            if line.startswith("mask"):
                self.mask = line[7:]
            else:
                key = line[line.index('[') + 1:line.index(']')]
                value = line.split("= ")[1]
                self.compute_one(key, int(value))

    def compute_one(self, key, value):
        num = 0
        for i in range(len(self.mask)):
            if self.mask[i] == 'X':
                num += int(pow(2, 35 - i)) if ((value & int(pow(2, 35 - i))) == int(pow(2, 35 - i))) else 0
            elif self.mask[i] == '1':
                num += int(pow(2, 35 - i))
        self.results[key] = num

    def sum(self):
        s = 0
        for key in self.results.keys():
            s += self.results[key]
        return s


with open("input.txt", "r") as f:
    l = [x.strip() for x in f.readlines()]

Docking(l)
