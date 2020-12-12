class SeatingSystem:

    def __init__(self, data):
        self.data = data
        self.positions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def check(self, x, y, c):
        counter = 0
        for (offsetX, offsetY) in self.positions:
            if self.validPosition(x + offsetX, y + offsetY):
                if self.data[x + offsetX][y + offsetY] == c:
                    counter += 1
        return counter

    def validPosition(self, x, y):
        return 0 <= x < len(self.data) and 0 <= y < len(self.data[0])

    def round(self):
        newList = []

        for x in range(len(self.data)):
            newLine = []
            for y in range(len(self.data[0])):
                if self.data[x][y] == '.':
                    newLine.append('.')
                if self.data[x][y] == '#':
                    newLine.append('L' if self.check(x, y, '#') >= 4 else '#')
                if self.data[x][y] == 'L':
                    newLine.append('#' if self.check(x, y, '#') == 0 else 'L')
            newList.append(newLine)
        return newList

    def run(self):
        while True:
            newData = self.round()
            if newData == self.data:
                return sum([x.count('#') for x in newData])
            self.data = newData


with open("input.txt", "r") as f:
    l = [[f for f in x] for x in f.read().split()]
    print(SeatingSystem(l).run())
