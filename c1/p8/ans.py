print((lambda n, k, arr: (lambda k, mod_arr: (lambda freq, mod_arr, k: sum([sum([freq[k - mod_arr[i]] if k - mod_arr[i] in freq else 0, freq[0] - 1 if 0 in freq and mod_arr[i] == 0 else 0]) for i in range(len(mod_arr))]))((lambda arr: (lambda freq, arr: (lambda freq, arr, garb: {i : len(freq[i]) for i in set(arr)})(freq, arr, [freq[i].append(0) for i in arr] != 0))({i: [] for i in set(arr)}, arr))(mod_arr), mod_arr, k))(k, list(map(lambda x: x % k, arr))))(*(lambda input: [*map(int, input().split()), list(map(int, input().split()))])(__import__('sys').stdin.readline)) // 2)

# n, k = map(int, input().split())
# food = list(map(int, input().split()))
# freq = {}
# ans = 0
# for i in range(n):
#     food[i] %= k
#     if (k - food[i]) % k in freq:
#         ans += freq[(k - food[i]) % k]
#     if food[i] not in freq:
#         freq[food[i]] = 1
#     else:
#         freq[food[i]] += 1
# print(ans)