# 24
a python program to calculate answers to the 24 card game 

For now, I have this set up:
Four cards, named a, b, c, d

This program has two ways (named result1 and result2) to calculate 24:
result 1 attempts (ab)(cd) and adds operands between the letters
result 2 attempts (((ab)c)d) and also adds operands

In theory, these two ways should be able to calculate all possible 24 combinations, but it might take a very long time. 

I would like for my program to be able to simultaneously calculate 4 different results

Example: (normal)
2359

(2x3)(9-5) = 6x4 = 24

In this case the case is (axb)x(d-c), with original structure of ab dc

My ideal program will calculate first 2359, then 3592, 5923, 9235 and add operands between them simultaneously, because sometimes a certain order of number just don't work.

There are, of course, also solutions requiring triplets, such as 3252

The solution is:
3x((5x2)-2) = 3x(10-2) = 3x8 = 24

But the algorithm might be able to figure it out by aiming at making all 32 combinations and replacing the operations between a,b,c and d

The way I did it was to use a dictionary with operands. The process is then roughly :

sum(sum(a, b), sum(c, d)) for (a+b)+(c+d)

Then, usign some counters, I can swap the operands for anything I want until it finds 1 that gives 24.
