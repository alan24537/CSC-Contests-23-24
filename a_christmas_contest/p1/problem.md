# Problem 1: Delivering Presents

**Time Limit:** 1s
**Memory Limit:** 128MB

Contrary to popular belief, Santa Claus does not have all the presents stored at the North Pole. Instead, he has a bunch warehouses scattered around the world where each warehouse stores $P$ presents. Santa Claus also has a path in the form of a list of locations. The path contains $N$ locations each of which are either a children's house (`H`) or a warehouse (`W`). If the location is a children's house, Santa Claus must deliver 1 present. If the location is a warehouse, Santa Claus can pick up at most $P$ presents to put in his magic bag, which can hold an unlimited amount of presents. Santa Claus starts at the first location in the path and must visit each location in order. Help Santa Claus determine if he can deliver a present to each children's house.

## Constraints

$1 \leq N \leq 2000$
$1 \leq P \leq 100$

## Input Specification

The first line of input will contain two integers, $N$ and $P$, the number of warehouses, the number of locations in the path and the number of presents at each warehouse. The next line will contain $N$ characters, representing the path.

## Output Specification

Output `YIPEE` if Santa Claus can deliver a present to each children's house. Otherwise, output `OH NO`.

## Sample Input 1

```txt
9 2
WWHHHWHHH
```

## Sample Output 1

```txt
YIPEE
```

## Sample Input 2

```txt
10 2
WWHHHWHHHH
```

## Sample Output 2

```txt
OH NO
```
