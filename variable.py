class variable:
	def __init__(self,name,state):
		self.name=name
		self.state=state
		self.gates=[]
	def update(self,value):
		if value != self.state:
			self.state=value
			print(self.name," will change to",value)
			for i in self.gates:
				i.refresh() 
		else:
			print(self.name, "did not change")
	def __str__(self):
		return self.name+"|"+str(self.state)

variables={}
variables["A"]=variable("A",0)
variables["B"]=variable("B",0)
variables["C"]=variable("C",0)

