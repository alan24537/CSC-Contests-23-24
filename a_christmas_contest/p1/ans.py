import sys
N, P = map(int, input().split())
s = input().strip()

prizes = 0

for i in s:
    if i == "W": prizes += P
    else: prizes -= 1

print("YIPEE" if prizes >= 0 else "OH NO")