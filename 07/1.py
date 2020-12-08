def parse(l):
    dic = {}
    for line in l:
        contains = line.split("contain")
        bags = contains[1].split(",")
        for i in range(len(bags)):
            bags[i] = bags[i].lstrip().lstrip('0123456789').lstrip().rstrip("s")
        dic[contains[0].rstrip().rstrip("s")] = bags
    dic["no other bag"] = []
    return dic






with open("input.txt", "r") as f:
    l = f.read().split(".\n")
    l[-1] = l[-1].strip(".")

dic = parse(l)


def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


p = {}

for k, v in dic.items():
    p.setdefault(k, [])
    for x in v:
        p.setdefault(x, []).append(k)

s = set()
dfs(s, p, "shiny gold bag")

s.remove("shiny gold bag")
print(len(s))









# for item in dic.keys():
#     visited = set()
#     if item not in s:
#         dfs(visited, dic, item)
#         if "shiny gold bag" in visited:
#             s = s.union(visited)
# s.remove()
