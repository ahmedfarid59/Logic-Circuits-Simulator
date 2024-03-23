import re
from .components import  getComponents
from  .variable import variable 
from sys import argv

if len(argv) ==4:
	lib=argv[1]
#getting the dictionary of components
components=getComponents(lib)

class gate:
	"""
	the gate class which holds the inputs and output variables
	it holds also the respective component
	"""
	def __init__(self,name,comp,outVar, *args):
		self.name=name
		self.component=comp
		self.outVar=outVar
		self.inputs=args
	def refresh(self):
		"""function to run the gate to update the output  wire  or variable"""
		bits =[x.state for x in self.inputs]
		self.outVar.update(self.component.run([ x for x in bits]),0,self.component.delay)
	def __str__(self):
		return self.name + "|"+self.component.name

def getVars(circuits):
	"""
	the function that takes the circuit file and construct the variables objects
	returns a dictionary with the variables and wires to be used 
	it also populates every gate with its inputs and output variables and wires
	"""
	variables={}
	with open(circuits,"r") as cir:
		for line in cir:
			lst=line.strip().replace(" ","").upper().split(",")
			if len(lst) == 1 :
				if len(lst[0])==1:
					variables[lst[0]]=variable(lst[0],0)
			else:
				vn=lst[2]
				if vn not in variables:
					variables[vn]=variable(vn,0)
				com=components[re.sub("\d","",lst[1])]
				g=gate(lst[0],com,variables[vn],*[variables[x] for x in lst[3:]])
				g.refresh()
				for v in lst[3:]:
					variables[v].gates.append(g)
	return variables
