l = []

with open("input.txt", "r") as f:
    for line in f:
        l.append(line.strip())

count = 0
x = 3
y = 1

while y < len(l):
    if l[y][x % len(l[0])] == "#":
        count += 1
    x += 3
    y += 1
print(count)


