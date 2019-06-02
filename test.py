import itertools
import numpy as np
import operator



A = input("card 1; ")
B = input("card 2; ")
C = input("card 3; ")
D = input("card 4; ")

def checker(a, b, c, d):  # needs work
	ops = {
		"+": operator.add,
		"-": operator.sub,
		"*": operator.mul,
		"/": operator.truediv,
		"^": operator.pow
	}

	op1 = "+"
	op2 = "-"
	op3 = "*"
	op4 = "/"
	op5 = "^"
	
	if ops[op_char2]((ops[op_char1](a, b)), (ops[op_char3](c, d))) = 24: # a +1 b +2 c +3 d
		print(a, op_char1, b, op_char2, c, op_char3, d, " = 24")

	# op_char = input('enter a operand')
	# op_func = ops[op_char]
	# result = op_func(x, y)

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
		checker(a, b, c, d)

all_pairs([A, B, C, D])
