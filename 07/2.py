def parse(l):
    dic = {}

    for line in l:
        contains = line.split("contain")
        bags = contains[1].split(",")
        counts = []
        for i in range(len(bags)):
            if "no other bags" not in bags[0]:
                counts.append((bags[i].lstrip().lstrip('0123456789').lstrip().rstrip("s"),
                               int(bags[i][1:len(bags[i]) - 1 - len(bags[i].lstrip(' 0123456789'))])))
            else:
                counts.append(("no other bag", 1))
        dic[contains[0].rstrip().rstrip("s")] = counts
    dic["no other bag"] = []
    return dic


with open("input.txt", "r") as f:
    l = f.read().split(".\n")
    l[-1] = l[-1].strip(".")

dic = parse(l)


def dfs(graph, node):
    count = 0
    for neighbour in graph[node]:
        if dic[neighbour[0]][0][0] == "no other bag":
            count += neighbour[1]
        else:
             count += neighbour[1] + neighbour[1] * dfs(graph, neighbour[0])
    return count


print(dfs(dic, "shiny gold bag"))
