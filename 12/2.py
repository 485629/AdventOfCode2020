class PASystem:

    def __init__(self, data):
        self.instructions = data
        self.north = 0
        self.east = 0
        self.waypoint = [1, 10]

    def change_direction(self, side, degrees):
        degrees = (360 - degrees) // 90 if side == 'L' else degrees // 90
        if degrees == 1:
            self.waypoint = [-self.waypoint[1], self.waypoint[0]]
        if degrees == 2:
            self.waypoint = [-self.waypoint[0], -self.waypoint[1]]
        if degrees == 3:
            self.waypoint = [self.waypoint[1], -self.waypoint[0]]

    def compute(self):
        for i in range(len(self.instructions)):
            c = self.instructions[i][0]
            if c == 'F':
                self.north += self.waypoint[0] * self.instructions[i][1]
                self.east += self.waypoint[1] * self.instructions[i][1]
            if c == 'R' or c == 'L':
                self.change_direction(c, self.instructions[i][1])
            if c == 'N' or c == 'S':
                self.waypoint[0] += self.instructions[i][1] if c == 'N' else -self.instructions[i][1]
            if c == 'E' or c == 'W':
                self.waypoint[1] += self.instructions[i][1] if c == 'E' else -self.instructions[i][1]

    def run(self):
        self.compute()
        print(abs(self.north) + abs(self.east))


with open("input.txt", "r") as f:
    l = [[x[0], int(x[1:])] for x in f.read().split()]

mySystem = PASystem(l)
mySystem.run()
