class gate:
	def __init__(self,name,comp,outVar, *args):
		self.name=name
		self.component=comp
		self.outVar=outVar
		self.inputs=args
	def refresh(self):
		print(self.name)
		self.outVar.update(self.component.run(self.inputs))
