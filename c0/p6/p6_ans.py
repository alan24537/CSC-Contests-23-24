import sys
input = sys.stdin.readline
n, q, c = map(int, input().split())
menu = list(map(int, input().split()))
psa = [0 for i in range(n + 5)]
for i in range(1, n + 1):
    psa[i] = psa[i - 1] + menu[i - 1] if menu[i - 1] <= c else psa[i - 1]
for i in range(q):
    a, b = map(int, input().split())
    print(psa[b] - psa[a - 1])