l = []
with open("input1.txt", "r") as f:
    for line in f:
        l.append(int(line.strip()))
print(l)

for i in range(len(l)):
    for j in range(1, len(l)):
        if l[i]+l[j] == 2020:
            print(l[i]*l[j])