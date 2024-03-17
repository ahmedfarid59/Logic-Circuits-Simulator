from .components import  getComponents
from  .variable import variable 

components=getComponents("lib.lib")

class gate:
	def __init__(self,name,comp,outVar, *args):
		self.name=name
		self.component=comp
		self.outVar=outVar
		self.inputs=args
	def refresh(self):
		bits =[x.state for x in self.inputs]
		print(self.name,self.component,"updating the variable", self.outVar ,"by",bits)
		self.outVar.update(self.component.run([ x for x in bits]),self.component.delay)
	def __str__(self):
		return self.name + "|"+self.component.name


def getVars(circuits):
	variables={}
	with open(circuits,"r") as cir:
		for line in cir:
			lst=line.strip().replace(" ","").split(",")
			if len(lst) == 1 :
				if len(lst[0])==1:
					variables[lst[0]]=variable(lst[0],0)
			else:
				vn=lst[2]
				if vn not in variables:
					variables[vn]=variable(vn,0)
				g=gate(lst[0],components[lst[1]],variables[vn],*[variables[x] for x in lst[3:]])
				g.refresh()
				for v in lst[3:]:
					variables[v].gates.append(g)
	return variables
