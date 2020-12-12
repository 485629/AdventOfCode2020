class PASystem:

    def __init__(self, data):
        self.facing = 'E'
        self.instructions = data
        self.north = 0
        self.east = 0

    def change_direction(self, side, degrees):
        directions = ['N', 'E', 'S', 'W']
        if side == 'L':
            degrees = 360 - degrees
        self.facing = directions[(directions.index(self.facing) + degrees // 90) % 4]

    def compute(self):
        for i in range(len(self.instructions)):
            c = self.instructions[i][0]
            if c == 'F':
                c = self.facing
            if c == 'R' or c == 'L':
                self.change_direction(c, self.instructions[i][1])
            if c == 'N' or c == 'S':
                self.north += self.instructions[i][1] if c == 'N' else -self.instructions[i][1]
            if c == 'E' or c == 'W':
                self.east += self.instructions[i][1] if c == 'E' else -self.instructions[i][1]

    def run(self):
        self.compute()
        print(abs(self.north) + abs(self.east))


with open("input.txt", "r") as f:
    l = [[x[0], int(x[1:])] for x in f.read().split()]

PASystem(l).run()
