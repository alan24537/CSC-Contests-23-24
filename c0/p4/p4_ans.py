n, k = int(input()), int(input())
ratings = [int(input()) for i in range(n)]
ratings.sort(reverse=True)
print(sum(ratings[:k]))