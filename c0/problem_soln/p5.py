n, q = map(int, input().split())

shops = []
for i in range(n):
    shop = input().split()
    shops.append([shop[0], int(shop[1])])
    
print(shops)
    
for i in range(q):
    x = int(input())
    ans = ["", 1e9]
    for shop in shops:
        if abs(shop[1] - x) < abs(ans[1] - x):
            ans = shop
    print(ans[0])