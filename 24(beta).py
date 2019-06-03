import itertools
import operator
# import tkinter  # not used for now

A = input("card 1; ")
B = input("card 2; ")
C = input("card 3; ")
D = input("card 4; ")

def checker(a, b, c, d):
	ops = {
		"+": operator.add,
		"-": operator.sub,
		"*": operator.mul,
		"/": operator.truediv,
		"^": operator.pow
	}
	op = ["+", "-", "*", "/", "^"]
	for i in itertools.product([0, 1, 2, 3, 4], repeat=3):

		m = i[0]
		n = i[1]
		o = i[2]
		op_char1 = op[m]
		op_char2 = op[n]
		op_char3 = op[o]

		try:
			result1 = ops[op_char2]((ops[op_char1](a, b)), (ops[op_char3](c, d)))  # a +1 b +2 c +3 d
			result2 = ops[op_char3]((ops[op_char2]((ops[op_char1](a, b)), c)), d)
			# result3 = ops[op_char1]([a, b, c, d], 0)
			if result1 is 24:
				print("(", a, op_char1, b, ")", op_char2, "(", c, op_char3, d, ")", "= 24")
				exit()
			if result2 is 24:
				print("(", a, op_char1, b, op_char2, c, ")", op_char3, d, "= 24")
				exit()
			# if result3 is 24:
				# print(a, op_char1, b, op_char1, c, op_char1, d)
		except ZeroDivisionError:
			pass
		except OverflowError:
			pass

def flatten(x):
	return list(itertools.chain(*x))

def all_pairs(lst):
	for p in itertools.permutations(lst):
		i = iter(p)
		zipped = (zip(i, i))
		alll = list(zipped)
		flattened = (flatten(alll))
		results = list(map(int, flattened))
		a = results[0]
		b = results[1]
		c = results[2]
		d = results[3]
		checker(a, b, c, d)
all_pairs([A, B, C, D])
