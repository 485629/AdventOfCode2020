with open("input.txt", "r") as f:
    l = [int(x) for x in f.read().split()]
    l.sort()

diffs = [l[i] - l[i-1] for i in range(1, len(l))]
print((diffs.count(1) + 1) + (diffs.count(3) + 1))
