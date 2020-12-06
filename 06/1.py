with open("input.txt", "r") as f:
    x = f.read().split("\n\n")
    counter = 0
    for item in x:
        s = set()
        item = item.replace('\n', '').strip()
        for character in item:
            s.add(character)
        counter += len(s)
print(counter)
