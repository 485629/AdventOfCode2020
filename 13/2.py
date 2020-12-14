from functools import reduce

with open("input.txt", "r") as f:
    f.readline()
    l = f.read().split(",")

l = [int(x) if x.isdigit() else x for x in l]
indexes = []
for i in range(0, len(l)):
    if l[i] != "x":
        indexes.append(i)


modulos = [l[i] for i in indexes]
numbers = [0 if indexes[i] == 0 else modulos[i] - (indexes[i] % modulos[i]) for i in range(len(indexes))]



def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == '__main__':
    print(chinese_remainder(modulos, numbers))

