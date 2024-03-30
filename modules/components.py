import re
 
class component:
	"""	class for the components (.lib file)
	stores the component name, number of inputs , expressions and delay	"""
	def __init__(self,name,noi,expression,delay):
		self.name=name
		self.noi=noi
		self.expression=expression.replace("|"," or ").replace("&"," and ").replace("~"," not ")
		self.delay=delay
	def run(self,args):
		"""the function which evaluates the inputs based on the component name""" 
		exp=self.expression
		vars=re.findall("I\d",exp)
		for i,v in enumerate(args):
			exp=exp.replace(vars[i],str(args[i]))
		exec("global result\nresult= "+ exp)
		return result
	def __str__(self):
		return self.name

def getComponents(path):
	"""
	a function for reading the library file and construct the object from the component class
it takes the path of the file as an argument 
and returns dictionary with the components along with their names
	"""
	components={}
	with open(path,"r") as lib:
		for line in lib:
			lst=line.strip().replace(" ","").upper().split(",")
			components[lst[0]]=component(lst[0],int(lst[1]),lst[2],int(lst[3]))
	return components