# Problem 7: Litter Box Placing

**Time Limit:** 1s

Jacob is trying to figure out where to place his litter box in the optimal spot. At the same time, he also needs to put the food and water bowls somewhere. He read online that you should try and place the litter box as far away from the food and water bowls as possible. Jacob has managed to model his house as a 2D plane and has $N$ possible locations for the litter box, $(L_x, L_y)$, and $M$ possible locations for the food and water bowls $(F_x, F_y)$. He wants to know where to place the litter box and food and water bowls such that the distance between the litter box and food and water bowl is maximized.

## Constraints

$1 \leq N, M \leq 10^3$
$-10^4 \leq L_x, L_y, F_x, F_y \leq 10^4$

It is guaranteed that there will never be a tie for the maximum distance.

## Input Specification

The first line will contain 2 space separated integers $N$ and $M$. The next $N$ lines will contain 2 space separated integers $L_x$ and $L_y$. The next $M$ lines will contain 2 space separated integers $F_x$ and $F_y$.

## Output Specification

The first line of output should contain 2 space separated integers $L_x$ and $L_y$ representing the location of the litter box. The second line of output should contain 2 space separated integers $F_x$ and $F_y$ representing the location of the food and water bowls.

## Sample Input

```txt
3 2
0 5
-9 4 
4 6
7 1
2 1
```

## Sample Output

```txt
-9 4
7 1
```
