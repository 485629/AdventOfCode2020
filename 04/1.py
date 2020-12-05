

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

class Passport:
    valid = False
    data = []

    def __init__(self, str):
        self.data = str.replace('\n', ' ').split()
        self.data.sort()
        self.fields = ["byr:", "cid:", "ecl:", "eyr:", "hcl:", "hgt:", "iyr:", "pid:"]

    def check(self):
        if len(self.data) == 7:
            offset = 1
        else:
            offset = 0
        if not self.data[0].startswith(self.fields[0]):
            return False
        for index in range(1, len(self.data)):
            if not self.data[index].startswith(self.fields[index + offset]):
                return False

        return True



    def isValid(self):
        if len(self.data) == 8:
            return self.check()
        if len(self.data) == 7:
            if not self.data[1].startswith("cid"):
                return self.check()
        return False



with open("input.txt", "r") as f:
    x = f.read().split("\n\n")
    print(len(x))

l = []
for item in x:
    l.append(Passport(item).isValid())
print(l.count(True))

















