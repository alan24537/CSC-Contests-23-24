# Problem 2: Building the Christmas Tree

**Time Limit:** 1s
**Memory Limit:** 128MB

Jacob is in a very festive mood, and wants to wish everyone a Merry Christmas. He decides to build a Christmas tree out of asterisks (`*`). The tree will be $N$ sections tall where each section is 4 lines tall. The first section will be 1 asterisk, then 3, then 7, then 11. The first line of each section after the first will start with 6 lesson asterisks than the last line of the previous section, then increase in the same pattern of the first section. After the $N$ sections, the base of the tree will be 5 lines tall and 3 hashtags (`#`) wide. The tree must be centered in the output.

## Constraints

$1 \leq N \leq 100$

## Input Specification

There will be one line of input, containing the integer $N$.

## Output Specification

Output the Christmas tree as described above.

## Sample Input

```txt
3
```

## Sample Output

```txt
          *
         ***
       *******
     ***********
       ******
      ********
    ************
  ****************
     ***********
    *************
  *****************
*********************
         ###
         ###
         ###
         ###
         ###
```
