# Problem 5: Help The Elf Get Home

**Time Limit:** 1s
**Memory Limit:** 128MB

Being so close to Christmas, our elf, Twinkleberry Bumblepuff, has been working overtime to make sure that all the presents are ready to be delivered. After working his 40 hours today, he is ready to go home and take a *short* nap. Unfortunately, the normal path he takes to get home is blocked by presents! Fortunately, his friend, Snickerdoodle Sparkletoes, has a map that marks his current location, all the presents and his home. The map is a grid of size $N \times M$ where each cell is either empty, a present or his home. Twinkleberry Bumblepuff starts on the cell marked with `E` and his home is marked with `H`. Empty cells are marked with `.` and presents are marked with `X`. Twinkleberry Bumblepuff can only move up, down, left or right and cannot move onto a cell with a present. Help Twinkleberry Bumblepuff find the shortest path to his home so he can take his nap!

## Constraints

$2 \leq N, M \leq 2000$

## Input Specification

The first line of input will contain two integers, $N$ and $M$, the dimensions of the map. The next $N$ lines will contain $M$ characters each, representing the map.

## Output Specification

Output the length of the shortest path from Twinkleberry Bumblepuff's current location to his home. If there is no path, output `-1`.

## Sample Input

```txt
4 8
E.....X.
X.XX..XX
XXX..XXX
H......X
```

## Sample Output

```txt
11
```
