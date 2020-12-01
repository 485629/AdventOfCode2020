l = []
with open("input1.txt", "r") as f:
    for line in f:
        l.append(int(line.strip()))
print(l)

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if l[i]+l[j]+l[k] == 2020:
                print(l[i]*l[j]*l[k])