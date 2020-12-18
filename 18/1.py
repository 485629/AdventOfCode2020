class Calculator:

    def __init__(self, examples):
        self.examples = examples
        self.compute_all()



    def compute_all(self):
        print(sum([self.compute_one(x) for x in self.examples]))


    def compute_one(self, example):
        temp_sum = 0
        first = True
        plus = True
        i = 0
        while i < len(example):
            if example[i] == "(":
                s = self.matching_brackets(example, i, len(example))
                if first:
                    temp_sum = self.compute_one(example[i + 1:s])
                    first = False
                else:
                    temp_sum = temp_sum + self.compute_one(example[i + 1:s]) if plus \
                        else temp_sum * self.compute_one(example[i + 1:s])
                i = s + 1
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
                            temp_sum *= int(example[i])
                elif example[i] == "+":
                    plus = True
                else:
                    plus = False
                i += 1
        return temp_sum



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