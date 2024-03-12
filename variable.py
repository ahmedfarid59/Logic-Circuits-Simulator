class variable:
	def __init__(self,name,state):
		self.name=name
		self.state=state
		self.gates=[]
	def update(self,value):
		if value != self.state:
			self.state=value
			print(self.name,self.state)
			for i in self.gates:
				i.refresh() 
	def __str__(self):
		return self.name+"|"+str(self.state)
