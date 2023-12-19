# Problem 4: Secret Santa

**Time Limit:** 1s
**Memory Limit:** 128MB

Getting into the festive spirit, you and your $N$ friends decide to host a secret santa gift exchange. You have been tasked with figuring out how to do the gift exchange. You decide on having one random starting person who gives their gift to their secret santa. Then, the person who received the gift gives their gift to their secret santa, and so on. You soon realize that this will loop back to the first person, and you will have to randomly choose a new starting person. You want to know the number of time you will have to randomly choose a new starting person.

Given the list of people and their secret santa, determine the number of times you will have to randomly choose a new starting person.

## Constraints

$2 \leq N \leq 10\space000$

Each name will be at most 20 characters long and will only contain lowercase letters.

## Input Specification

The first line will contain the integer $N$, the number of people in the gift exchange. The next $N$ lines will contain two strings, the name of the person and the name of their secret santa. It is guaranteed that each name will be unique and that each person will receive and give exactly one gift.

## Output Specification

Output the number of times you will have to randomly choose a new starting person.

## Sample Input

```txt
5
Alice Bob
Bob Charlie
Charlie Alice
David Eve
Eve David
```

## Sample Output

```txt
2
```
