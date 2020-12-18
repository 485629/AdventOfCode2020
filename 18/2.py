class Calculator:

    def __init__(self, examples):
        self.examples = examples
        self.compute_all()

    def compute_all(self):
        print(sum([self.compute_one(x)[0] for x in self.examples]))

    def compute_one(self, example):
        temp_sum = 0
        first = True
        plus = True
        i = 0
        while i < len(example):
            if example[i] == "(":
                s = self.matching_brackets(example, i, len(example))
                if first:
                    num, new_i = self.compute_one(example[i + 1:s])
                    temp_sum = num
                    first = False
                else:
                    if plus:
                        num, new_i = self.compute_one(example[i + 1:s])
                        temp_sum = temp_sum + num
                    else:
                        num, new_i = self.compute_one(example[i:])
                        temp_sum = temp_sum * num
                        new_i -= 1
                i += new_i + 2
            elif example[i] == ")":
                i += 1
                continue
            else:
                if example[i].isdigit():
                    if first:
                        temp_sum = int(example[i])
                        first = False
                    else:
                        if plus:
                            temp_sum += int(example[i])
                        else:
                            if i == len(example) - 1:
                                temp_sum *= int(example[i])
                                return temp_sum, i
                            num, new_i = self.compute_one(example[i:])
                            temp_sum *= num
                            i += new_i
                elif example[i] == "+":
                    plus = True
                else:
                    plus = False
                i += 1
        return temp_sum, i - 1

    def matching_brackets(self, example, start, end):
        counter = 1
        for i in range(start + 1, end):
            if example[i] == "(":
                counter += 1
            if example[i] == ")":
                counter -= 1
            if counter == 0:
                return i


with open("input.txt", "r") as f:
    examps = [[k for k in x if k != " "] for x in f.read().split("\n")]

# print(*list(examps), sep="\n")


Calculator(examps)
