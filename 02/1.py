l = []

with open("input.txt", "r") as f:
    for line in f:
        l.append(line.strip())

count = 0

for line in l:
    splited = line.split()
    nums = splited[0].split("-")
    splited[1] = splited[1][0]
    letterCount = splited[2].count(splited[1])
    if letterCount >= int(nums[0]) and letterCount <= int(nums[1]):
        count += 1

print(count)    