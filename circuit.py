import re

lib=open("lib.lib","r")
components={}
inputs={}


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
	def switch(self,value):
		state=value
		for i in self.gates:
			i.refresh()

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

for line in lib:
	lst=line.strip().split(",")
	components[lst[0]]=component(lst[0],int(lst[1]),lst[2],int(lst[3]))

class gate:
	def __init__(self,name,output,*args):
		self.component=components[name]
		if output not in inputs :
			inputs[output]=input(output,0)
		self.arguments=args
	def run(self):
		inputs[output].state=self.component.run(self.arguments)
		inputs[output].refresh()