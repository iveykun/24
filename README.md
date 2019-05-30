# 24
a python program to calculate answers to the 24 card game 

For now, I have this set up:
Four cards, named a, b, c, d

There are 32 possibilities in total:

ab cd
ab dc
ac bd
ad bc
ac db
ad cb

ba cd
ba dc
bc ad
bc da
bd ca
bd ac

ca bd
ca db
cb ad
cb da
cd ba
cd ab

da bc
da cb
db ac
db ca
dc ab
dc ba

I think it is possible to calculate every solution using pairs (a,b) and (c,d) to make sums, differences and products.

for example, a common technique is to find (4,6). The program would then run through the 32 possibilities to find sums and products that will result in a 6 or a 4.

Example: 
23 59

(2x3)(9-5) = 6x4 = 24

In this case the case is (axb)x(d-c), with original structure of ab dc
