class variable:
	def __init__(self,name,state):
		self.name=name
		self.state=state
		self.gates=[]
	def update(self,value):
		if value != self.state:
			self.state=value
			time=0
			for i in self.gates:
				time+=i.refresh() 
				return time
	def __str__(self):
		return self.name+"|"+str(self.state)

variables={}
variables["A"]=variable("A",0)
variables["B"]=variable("B",0)
variables["C"]=variable("C",0)

