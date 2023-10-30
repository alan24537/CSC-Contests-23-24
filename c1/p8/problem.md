# Problem 8:

**Time Limit:** 1s
**Memory Limit:** 128MB

Jacob loves his new cat very much. As such, he want to make sure that his cat stays inside of his house. Jacob's house is a bit peculiar, as it is shaped like a triangle and can be models with a 2D plane. He attached a GPS tracker to his cat, and he wants to know if his cat is inside of his house. Given the coordinates of the three vertices of Jacob's house $(A_x, A_y), (B_x, B_y), ([C_x, C_y)$ and the coordinates of his cat, $(P_x, P_y)$ determine if his cat is inside of his house.

**Hint:** You may need to use the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) to solve this problem.

The area of triangle $ABC$ is given by the following formula:

$A = \frac{1}{2} \left| (A_x B_y + B_x C_y + C_x A_y) - (A_y B_x + B_y C_x + C_y A_x) \right|$

## Constraints

$-10^3 \leq A_x, A_y, B_x, B_y, C_x, C_y, P_x, P_y \leq 10^3$

## Input Specification

The first line of input will contain the coordinates of the three vertices of Jacob's house, $A_x, A_y, B_x, B_y, C_x, C_y$. The second line of input will contain the coordinates of Jacob's cat, $P_x, P_y$.

## Output Specification

Output `yes` if Jacob's cat is inside of his house, and `no` otherwise.

## Sample Input

```txt
-3 4 5 2 -1 -1
1 1
```

## Sample Output

```txt
yes
```
