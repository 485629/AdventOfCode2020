with open("input.txt", "r") as f:
    number = int(f.readline())
    l = list(filter(lambda a: a != "x", f.read().split(",")))
    l = [int(x) for x in l]


diff = [number // x * x + x - number for x in l]
print(l[diff.index(min(diff))] * min(diff))
