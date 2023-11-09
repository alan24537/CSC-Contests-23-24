# print((lambda n, k, arr: sum([(arr[i] + arr[j]) % k == 0 for i in range(n) for j in range(i + 1, n)]))(*map(int, input().split()), list(map(int, input().split()))))

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if (arr[i] + arr[j]) % k == 0:
#             ans += 1
# print(ans)

n,k = input().split()
n,k = int(n), int(k)
b = list(map(int, input().split()))
nofp = 0
for gi in b:
  for gj in b:
    if gi < gj:
      if ((gi+gj) % k) == 0:
        nofp += 1
print(nofp)