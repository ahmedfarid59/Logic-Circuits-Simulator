class input:
	def __init__(self,name,state):
		self.name=name
		self.state=state

class component:
	def __init__(self,name,noi,expression,delay):
		self.name=name
		self.noi=noi
		self.expression=expression
		self.delay=delay
	def run(self,*args):
		pass
        


