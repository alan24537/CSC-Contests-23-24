n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
freq = {}

for i in range(n):
    arr[i] %= k
    if arr[i] not in freq:
        freq[arr[i]] = 1
    else:
        freq[arr[i]] += 1
for i in range(n):
    if k - arr[i] in freq:
        ans += freq[k - arr[i]]
print(ans // 2)