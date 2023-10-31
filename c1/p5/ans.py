def solve():
    n = int(input())
    arr = [int(input()) for i in range(n)]

    arr.sort(reverse=True)
    for num in arr:
        if num != arr[0]:
            print(num)
            return
    print(-1)
    return

solve()