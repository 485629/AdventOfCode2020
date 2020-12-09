class XMAS:

    def __init__(self, data):
        self.data = data
        self.find = 41682220
        self.check()

    def check(self):
        for i in range(len(self.data)):
            num = 0
            for j in range(i, len(self.data)):
                num += self.data[j]
                if num == self.find:
                    print(min(self.data[i:j]) + max(self.data[i:j]))
                    return
                if num > self.find:
                    break


datas = []
with open("input.txt", "r") as f:
    for line in f:
        datas.append(int(line.strip()))

x = XMAS(datas)
