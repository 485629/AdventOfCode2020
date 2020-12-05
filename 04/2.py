
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
            return self.check() and self.validityCheck()
        if len(self.data) == 7:
            if not self.data[1].startswith("cid"):
                return self.check() and self.validityCheck()
        return False

    def validityCheck(self):
        l = [string.split(":") for string in self.data]
        valid = True
        for [field, value] in l:
            if field == "byr":
                if value.isdigit() is True:
                    valid = valid and 1920 <= int(value) <= 2002

            elif field == "iyr":
                if value.isdigit() is True:
                    valid = valid and 2010 <= int(value) <= 2020

            elif field == "eyr":
                if value.isdigit() is True:
                    valid = valid and 2020 <= int(value) <= 2030

            elif field == "hgt":
                metric = value.lstrip('0123456789')
                height = value[:len(value) - len(metric)]
                if metric == "in":
                    valid = valid and 59 <= int(height) <= 76
                elif metric == "cm":
                    valid = valid and 150 <= int(height) <= 193
                else:
                    return False

            elif field == "hcl":
                if len(value) == 7 and value[0] == "#":
                    for i in range(1, 7):
                        if not value[i].isdigit() and not (ord('a') <= ord(value[i]) <= ord('f')):
                            return False
                else:
                    return False

            elif field == "ecl":
                valid = valid and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

            elif field == "pid":
                valid = valid and value.isdigit() and len(value) == 9
            if valid is False:
                return False
        return valid










with open("input.txt", "r") as f:
    x = f.read().split("\n\n")
    print(len(x))

l = []
for item in x:
    l.append(Passport(item).isValid())
print(l.count(True))















