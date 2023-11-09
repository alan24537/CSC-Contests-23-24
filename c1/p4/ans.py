# print((lambda n: "meow" if sum(1 for _ in range(n) if int(input()) % 2 == 0) == n // 2 else "...")(int(input())))

n = int(input())
treats = [int(input()) for _ in range(n)]
even, odd = 0, 0
for treat in treats:
    if treat % 2 == 0:
        even += 1
    else:
        odd += 1
if even == odd:
    print("meow")
else:
    print("...")