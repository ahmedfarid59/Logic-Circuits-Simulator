import re


AND=re.compile("AND\d",re.IGNORECASE)
OR=re.compile("or\d",re.IGNORECASE)
NOT=re.compile("NOT",re.IGNORECASE)
XOR=re.compile("XOR\d",re.IGNORECASE)
NAND= re.compile("NAND\d")
NOR=re.compile("NOR\d",re.IGNORECASE)
XNOR=re.compile("XNOR\d",re.IGNORECASE)


class input:
	def __init__(self,name,state):
		self.name=name
		self.state=state
		self.gates=[]

class component:
	def __init__(self,name,noi,expression,delay):
		self.name=name
		self.noi=noi
		self.expression=expression
		self.delay=delay
	def run(self,*args):
		if re.fullmatch(AND,self.name) :
			return all(args)
		elif re.fullmatch(NAND,self.name):
			return not all(args)
		elif re.fullmatch(OR):
			return not all([ not x for x in args])
		elif re.fullmatch(NOR,self.name):
			return all([not x for x in args])
		elif re.fullmatch(XOR,self.name):
			return sum(args)%2 == 1
		elif re.fullmatch(XNor,self.name):
			return all(args) or all([not x for x in args])
		elif re.fullmatch(NOT,self.name):
			return not args[0]
