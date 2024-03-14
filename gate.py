class gate:
	def __init__(self,name,comp,outVar, *args):
		self.name=name
		self.component=comp
		self.outVar=outVar
		self.inputs=args
	def refresh(self):
		bits =[x.state for x in self.inputs]
		print(self.name,self.component,"updating the variable", self.outVar ,"by",bits)
		self.outVar.update(self.component.run([ x for x in bits]))
	def __str__(self):
		return self.name + "|"+self.component.name


