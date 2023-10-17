n = int(input())
d = int(input())

for i in range(n):
    c = int(input())
    if d - c < 0:
        print(i)
        d = 1e9
    d -= c