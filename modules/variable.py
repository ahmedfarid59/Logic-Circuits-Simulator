out=open("output.sim","w")
delay=0

class variable:
	def __init__(self,name,state):
		self.name=name
		self.state=state
		self.gates=[]
	def update(self,value,d):
		global delay
		if value != self.state:
			self.state=value
			delay+=d
			print(self.name," will change to",value)
			out.write(str(delay)+","+self.name+","+str(int(self.state))+"\n")
			for i in self.gates:
				i.refresh() 
		else:
			print(self.name, "did not change")
	def __str__(self):
		return self.name+"|"+str(self.state)

