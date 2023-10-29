# Problem 6:

**Time Limit:** 1s
**Memory Limit:** 128MB

Given a list of $N$ numbers, $A_i$, find the number of pairs of numbers $(A_i, A_j)$ such that $i < j$ and $A_i + A_j$ is divisible by $K$.

## Constraints

$2 \leq N \leq 10^3$
$1 \leq K \leq 10^9$
$1 \leq A_i \leq 10^9$

## Input Specification

The first line will contain 2 space separated integers $N$ and $K$. The next line will contain $N$ space separated integers $A_i$.

## Output Specification

Output the number of pairs of numbers $(A_i, A_j)$ such that $i < j$ and $A_i + A_j$ is divisible by $K$.

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
