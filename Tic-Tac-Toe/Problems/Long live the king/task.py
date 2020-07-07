c = int(input())
r = int(input())
corner = [(1, 1), (1, 8), (8, 1), (8, 8)]
if (c, r) in corner:
    print(3)
elif c in (1, 8):
    print(5)
elif r in (1, 8):
    print(5)
else:
    print(8)
