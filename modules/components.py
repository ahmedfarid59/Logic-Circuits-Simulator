from .utilities import evaluate
import re

class component:
	def __init__(self,name,noi,expression,delay):
		self.name=name
		self.noi=noi
		self.expression=expression
		self.delay=delay
	def run(self,args):
		return evaluate(self.name,args)
	def __str__(self):
		return self.name

def getComponents(path):
	components={}
	with open(path,"r") as lib:
		for line in lib:
			lst=line.strip().replace(" ","").upper().split(",")
			name=re.sub("\d","",lst[0])
			components[name]=component(name,int(lst[1]),lst[2],int(lst[3]))
	return components