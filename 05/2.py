class BoardingPass:
    row = 0
    column = 0
    seatID = 0

    def __init__(self, str):
        self.data = str
        self.setColumn()
        self.setRow()
        self.setSeatID()

    def setRow(self):
        self.row = 0
        for index in range(7):
            if self.data[index] == 'B':
                self.row += 2 ** (6 - index)

    def setColumn(self):
        self.column = 0
        for index in range(3):
            if self.data[index + 7] == 'R':
                self.column += 2 ** (2 - index)

    def setSeatID(self):
        self.seatID = self.row * 8 + self.column

    def getSeatID(self):
        return self.seatID


with open("input.txt", "r") as f:
    x = f.readlines()

l = []
for item in x:
    l.append(BoardingPass(item).getSeatID())


def findEmptySeat(list):
    for i in range(1, 127):
        for j in range(8):
            if i * 8 + j not in list:
                if i * 8 + j + 1 in list and i * 8 + j - 1 in list:
                    return i * 8 + j


print(findEmptySeat(l))
