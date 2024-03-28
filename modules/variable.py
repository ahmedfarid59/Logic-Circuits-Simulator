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
		#lists to hold the coordinates of the curve that will graph the variable state
	x=[0]
	y=[0]
	def update(self,value,t , d):
		"""the function that updates the variable and log the delay and timestam of the change """
		global delay#the integer variable that keeps track of the timestam
		if value != self.state:#to update and log only in case of different state
			delay+=t
			self.x.append(delay/50)
			self.y.append(int(self.state))
			self.state=value
			delay+=d#updating the delay variable
			self.x.append(delay/50)
			self.y.append(int(self.state))
			out.write(str(delay)+","+self.name+","+str(int(self.state))+"\n")
			#print(str(delay)+","+self.name+","+str(int(self.state))+"\n") I commented this line to avoid printing the output to the console as I only used it for testing :)
			#refreshing the respective gates
			for i in self.gates:
				i.refresh() 
	def __str__(self):
		return self.name+"|"+str(self.state)

