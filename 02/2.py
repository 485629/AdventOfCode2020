l = []

with open("input.txt", "r") as f:
    for line in f:
        l.append(line.strip())

count = 0

for line in l:
    splited = line.split()
    nums = splited[0].split("-")
    splited[1] = splited[1][0]
    letterCount = 0
    letterCount += 1 if splited[2][int(nums[0])-1] == splited[1] else 0
    letterCount += 1 if splited[2][int(nums[1])-1] == splited[1] else 0
    if letterCount == 1:
        count += 1

print(count)