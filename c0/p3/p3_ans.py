n = int(input())
d = int(input())
ans = 0
for i in range(n):
    c = int(input())
    d -= c
    if d >= 0:
        ans += 1
print(ans)