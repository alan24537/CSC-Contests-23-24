n = int(input())
d = int(input())
plates = [int(input()) for i in range(n)]
ans = 0
for plate in plates:
    d -= plate
    if d >= 0:
        ans += 1
print(ans)