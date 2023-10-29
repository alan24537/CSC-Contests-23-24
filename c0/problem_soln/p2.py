t1 = int(input())
t2 = int(input())
t3 = int(input())
x = int(input())

max_temp = max(t1, t2, t3)

print(max(0, max_temp - x))