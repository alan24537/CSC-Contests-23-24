n = int(input())
k = int(input())
ratings = [int(input()) for i in range(n)]

ratings.sort(reverse=True)

ans = 0
for i in range(k):
    ans += ratings[i]
print(ans)