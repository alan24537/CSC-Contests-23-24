print((lambda n, x: (x // n) + (x % n != 0))(int(input()), int(input())))

n = int(input())
x = int(input())
ans = x // n
if n % n != 0:
    ans += 1
print(ans)