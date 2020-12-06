with open("input.txt", "r") as f:
    x = f.read().split("\n\n")
    counter = 0
    for item in x:
        s = set()
        item = item.replace('\n', ' ').split()
        for character in item[0]:
            s.add(character)
        for index in range(1, len(item)):
            ns = set()
            for character in item[index]:
                ns.add(character)
            s = s.intersection(ns)
        counter += len(s)
print(counter)
