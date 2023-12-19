# Problem 3: Is it Christmas yet?

**Time Limit:** 1s
**Memory Limit:** 128MB

Christmas is an annual festival commemorating the birth of Jesus Christ, observed primarily on December 25 as a religious and cultural celebration among billions of people around the world. A feast central to the Christian liturgical year, it follows the season of Advent (which begins four Sundays before) or the Nativity Fast, and initiates the season of Christmastide, which historically in the West lasts twelve days and culminates on Twelfth Night. Christmas Day is a public holiday in many countries, is celebrated religiously by a majority of Christians, as well as culturally by many non-Christians, and forms an integral part of the holiday season surrounding it.

Alan is really excited for Christmas, but he is really bad at math, specifically telling what today's date is. He knows that Christmas is on December 25th, but he doesn't know how to tell if today is Christmas or not. Can you help him?

Given a date in the format of `YYYY/MM/DD`, tell Alan if today is Christmas, before Christmas, or after Christmas.

## Constraints

$1 ≤ YYYY ≤ 5000$
$1 ≤ MM ≤ 12$
$1 ≤ DD ≤ 31$

## Input Specification

The input will consist of a single line containing the date in the format of `YYYY/MM/DD`.

## Output Specification

Output a single line containing `Merry Christmas!` if the date is December 25th, `Not Yet ;-;` if it is before Christmas or `Too Late ;-;` if Christmas already passed.

## Sample Input 1

```txt
0001/12/25
```

## Sample Output 1

```txt
Not Yet ;-;
```

## Sample Input 2

```txt
2023/12/25
```

## Sample Output 2

```txt
Merry Christmas!
```
