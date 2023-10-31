# Problem 8: Finding the Cat

**Time Limit:** 1s

Jacob loves his new cat very much. As such, he want to make sure that his cat stays inside of his house. Jacob's house is a bit peculiar, as it is shaped like a triangle and can be models with a 2D plane. He attached a GPS tracker to his cat, and he wants to know if his cat is inside of his house. Given the coordinates of the three vertices of Jacob's house $(A_x, A_y), (B_x, B_y), (C_x, C_y)$ and the coordinates of his cat, $(P_x, P_y)$ determine if his cat is inside of his house.

**Hint:** You may need to use the area of a triangle to solve this problem. The area of triangle formed by the points $(A_x, A_y), (B_x, B_y), (C_x, C_y)$ is given by the following formula:

$AREA = \frac{1}{2} \left| (A_x B_y + B_x C_y + C_x A_y) - (A_y B_x + B_y C_x + C_y A_x) \right|$

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

## Explanation

<img src="https://cdn.discordapp.com/attachments/1091060345298235434/1168598342415171694/image.png?ex=65525904&is=653fe404&hm=42c36ec08a4d28f4212f54e5a51d98ac6ab1d0f26f8f7e01470cb700eab9c224&" width="300px">
