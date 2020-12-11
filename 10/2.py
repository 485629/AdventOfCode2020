import itertools

with open("input.txt", "r") as f:
    l = [int(x) for x in f.read().split()]
    l.append(0)
    l.append(max(l) + 3)
    l.sort()

def differences(my_list):
    return all(x < 4 for x in [my_list[i] - my_list[i - 1] for i in range(1, len(my_list))])

def count(my_list):
    c = 0
    stone = [my_list[0], my_list[-1]]
    for i in range(2, len(my_list)):
        for x in itertools.combinations(my_list, i):
            if x[0] == stone[0] and x[-1] == stone[-1] and differences(x):
                c += 1
    return c + 1

diffs = [l[i] - l[i-1] for i in range(1, len(l))]

counter = 0
result = 1
while counter < len(diffs):
    if diffs[counter] == 3:
        counter += 1
        continue
    if diffs[counter] == 1:
        x = len(list(itertools.takewhile(lambda x: x == 1, diffs[counter:])))
        if x > 1:
            result *= count(l[counter:counter+x+1])
        counter += x

print(result)

