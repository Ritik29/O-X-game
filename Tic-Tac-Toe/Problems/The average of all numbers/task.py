a = int(input())
b = int(input())
x = a
mean = []
m = 0
while x <= b:
    if x % 3 == 0:
        mean.append(x)
    x += 1
for i in mean:
    m += i / len(mean)
print(m)
