import re

AND=re.compile("AND\d*",re.IGNORECASE)
OR=re.compile("or\d*",re.IGNORECASE)
NOT=re.compile("NOT",re.IGNORECASE)
XOR=re.compile("XOR\d*",re.IGNORECASE)
NAND= re.compile("NAND\d*")
NOR=re.compile("NOR\d*",re.IGNORECASE)
XNOR=re.compile("XNOR\d*",re.IGNORECASE)

def evaluate(name,args):
	if re.fullmatch(AND,name) :
		return all(args)
	elif re.fullmatch(NAND,name):
		return not all(args)
	elif re.fullmatch(OR,name):
		return not all([ not x for x in args])
	elif re.fullmatch(NOR,name):
		return all([not x for x in args])
	elif re.fullmatch(XOR,name):
		return sum(args)%2 == 1
	elif re.fullmatch(XNOR,name):
		return sum(args)%2 == 0
	elif re.fullmatch(NOT,name):
		return not args[0]

