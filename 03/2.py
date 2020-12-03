l = []

with open("input.txt", "r") as f:
    for line in f:
        l.append(line.strip())

result = 1
nums = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for [x, y] in nums:
    count = 0
    x1 = x
    y1 = y
    while y < len(l):
        if l[y][x % len(l[0])] == "#":
            count += 1
        x += x1
        y += y1
    result *= count

print(result)
