# Problem 8: Mixing up Cat Food (Hard)

**Time Limit:** 1s

Jacob feels like his cat shouldn't only each 1 type of food. He wants to mix up the food a bit. He can buy $N$ cat food bags, each has $G_i$ grams of food. However, after some number of days, Jacob doesn't want leftover food. Given that Jacob's cat eats $K$ grams of food a day, find the number of pair of bags $(G_i, G_j)$ such that $i < j$ and $G_i + G_j$ is divisible by $K$?

## Constraints

Note the constraints are different from the original problem and you may need fast input for this problem.

$2 \leq N \leq 10^5$
$1 \leq K \leq 10^9$
$1 \leq G_i \leq 10^9$

## Input Specification

The first line will contain 2 space separated integers $N$ and $K$. The next line will contain $N$ space separated integers $G_i$.

## Output Specification

Output the number of pairs of numbers $(G_i, G_j)$ such that $i < j$ and $G_i + G_j$ is divisible by $K$.

## Sample Input

```txt
6 5
1 2 4 3 5 7
```

## Sample Output

```txt
3
```

## Explanation

The pairs are $(1, 4), (2, 3), (3, 7)$.
