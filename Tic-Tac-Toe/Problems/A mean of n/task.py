n = int(input())
x = []
tot = 0
c = 0
for _ in range(n):
    x = (int(input()))
    tot += x
    c += 1
print(tot / c)