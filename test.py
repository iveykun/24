import itertools

A = input("card 1; ")
B = input("card 2; ")
C = input("card 3; ")
D = input("card 4; ")

def checker(a, b, c, d):  # needs work
	if a


def flatten(x):
    return list(itertools.chain(*x))

def all_pairs(lst):
	for p in itertools.permutations(lst):
		i = iter(p)
		zipped = (zip(i, i))
		all = list(zipped)
		flattened = (flatten(all))
		results = list(map(int, flattened))
		a = (results)[0]
		b = (results)[1]
		c = (results)[2]
		d = (results)[3]
		#  print(results) will give you all possible combinations. You only need to change the operand between a, b, c and d.

all_pairs([A, B, C, D])
