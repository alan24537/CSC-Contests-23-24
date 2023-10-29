import sys
input = sys.stdin.readline

n, q = map(int, input().split())
claw = [list(map(int, input().split())) for i in range(n)]

claw.sort()

pma = []
pma.append(claw[0][1])
for i in range(1, n):
    pma.append(max(pma[i - 1], claw[i][1]))
    
for i in range(q):
    d = int(input())
    
    idx = -1
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if claw[mid][0] <= d:
            idx = max(idx, mid)
            lo = mid + 1
        else:
            hi = mid - 1
    print(pma[idx])