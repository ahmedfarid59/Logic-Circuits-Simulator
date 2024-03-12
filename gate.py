class gate:
	def __init__(self,name,comp,outVar, *args):
		self.name=name
		self.component=comp
		self.outVar=outVar
		self.inputs=args
	def refresh(self):
		print("updating the variable", self.outVar)
		time=self.outVar.update(self.component.run(self.inputs))
		print(self.component.delay,self.inputs,f"outputs to {self.outVar}")
	def __str__(self):
		return self.name + "|"+self.component.name


