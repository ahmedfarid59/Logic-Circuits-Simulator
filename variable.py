class variable:
	def __init__(self,name,state):
		self.name=name
		self.state=state
		self.gates=[]
	def update(self,value):
		if value != self.state:
			self.state=value
			print(self.name," will change to",value)
			time = 0
			for i in self.gates:
				time+=i.refresh() 
			return time
		else:
			print(self.name, "did not change")
			return 0
	def __str__(self):
		return self.name+"|"+str(self.state)

