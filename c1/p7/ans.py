n, m = map(int, input().split())
litter = [list(map(int, input().split())) for _ in range(n)]
food = [list(map(int, input().split())) for _ in range(m)]

def dist(x: tuple, y: tuple) -> float:
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    
ans_dist = -1
lans, fans = (0, 0), (0, 0)
for i in range(n):
    for j in range(m):
        if dist(litter[i], food[j]) > ans_dist:
            ans_dist = dist(litter[i], food[j])
            lans, fans = litter[i], food[j]
print(*lans)
print(*fans)