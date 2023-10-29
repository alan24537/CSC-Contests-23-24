n, q = map(int, input().split())
shops = []
for i in range(n):
    a, s = input().split()
    shops.append([a, int(s)])
for i in range(q):
    x = int(input())
    ans = ["", 1e9]
    for shop in shops:
        if abs(shop[1] - x) < abs(ans[1] - x):
            ans = shop
    print(ans[0])