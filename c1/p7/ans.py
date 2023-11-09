# print((lambda n, m, litter, food, dist_list: (type([dist_list.append([((litter[i][0] - food[j][0]) ** 2 + (litter[i][1] - food[j][1]) ** 2), litter[i], food[j]]) if (dist_list[len(dist_list) - 1][0] if len(dist_list) > 0 else -1) < ((litter[i][0] - food[j][0]) ** 2 + (litter[i][1] - food[j][1]) ** 2) else None for i in range(n) for j in range(m)]) == type([])) * (lambda dist_list: f"{dist_list[-1][1][0]} {dist_list[-1][1][1]}\n{dist_list[-1][2][0]} {dist_list[-1][2][1]}")(dist_list)) (*(lambda n, m, input: ([n, m, [list(map(int, input().split())) for _ in range(n)], [list(map(int, input().split())) for _ in range(m)], []]))(*map(int, input().split()), __import__("sys").stdin.readline)))

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