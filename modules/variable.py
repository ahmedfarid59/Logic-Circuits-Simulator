#opening the output file for loging the simulation
out=open("output.sim","w")
delay=0

class variable:
	"""the variable class that holds the variable or wire name and current state """
	def __init__(self,name,state):
		self.name=name
		self.state=state
		#the gates for which the instance variable or wire is an input to refresh them in case of any updates
		self.gates=[]
	def update(self,value,d):
		"""the function that updates the variable and log the delay and timestam of the change """
		global delay#the integer variable that keeps track of the timestam
		if value != self.state:#to update and log only in case of different state
			self.state=value
			delay+=d#updating the delay variable
			print(self.name," will change to",value)
			out.write(str(delay)+","+self.name+","+str(int(self.state))+"\n")
			#refreshing the respective gates
			for i in self.gates:
				i.refresh() 
		else:
			print(self.name, "did not change")
	def __str__(self):
		return self.name+"|"+str(self.state)

