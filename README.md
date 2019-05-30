# 24
a python program to calculate answers to the 24 card game 

For now, I have this set up:
Four cards, named a, b, c, d

There are 32 possibilities in total:

abcd/
abdc/
acbd/
adbc/
acdb/
adcb/

bacd/
badc/
bcad/
bcda/
bdca/
bdac/

cabd/
cadb/
cbad/
cbda/
cdba/
cdab/

dabc/
dacb/
dbac/
dbca/
dcab/
dcba/

And we can see that there are actually just 12 variations that make up that long list:

ab, ac, ad/
ba, bc, bd/
ca, cb, cd/
da, db, dc/

Which in turns makes it easier to just repeat the pattern twice to get the 32 possibilities
...
(might be possible to engineer a system that 'retires' a couple from the center and join the extremeties, in a (b,c)(a,d) fashion)
I think it is possible to calculate every solution using pairs (a,b) and (c,d) to make sums, differences and products.

for example, a common technique is to find (4,6). The program would then run through the 32 possibilities to find sums and products that will result in a 6 or a 4.

Example: 
2359

(2x3)(9-5) = 6x4 = 24

In this case the case is (axb)x(d-c), with original structure of ab dc

There are, of course, also solutions requiring triplets, such as 3252

The solution is:
3x((5x2)-2) = 3x(10-2) = 3x8 = 24

But the algorithm might be able to figure it out by aiming at making all 32 combinations and replacing the operations between a,b,c and d
