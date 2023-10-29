import sys
input = sys.stdin.readline

n, q, c = map(int, input().split())
menu = list(map(int, input().split()))

psa = []
psa.append(0)
for i in range(n):
    if menu[i] <= c:
        psa.append(psa[i] + menu[i])
    else:
        psa.append(psa[i])
        
for i in range(q):
    a, b = map(int, input().split())    
    print(psa[b] - psa[a - 1])