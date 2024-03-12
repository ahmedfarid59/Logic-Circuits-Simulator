from components import component , getComponents
from variable import variable
from gate import gate

components=getComponents("lib.lib")
variables={}
variables["A"]=variable("A",0)
variables["B"]=variable("B",0)
variables["C"]=variable("C",0)

cir=open("circuits.cir","r")

for line in cir:
	lst=line.strip().split(",")
	vn=lst[2]
	if vn not in variables:
		variables[vn]=variable(vn,0)
	g=gate(lst[0],components[lst[1]],variables[vn],*[variables[x].state for x in lst[3:]])
	for v in lst[3:]:
		variables[v].gates.append(g)

print("the operations")
delay=0
stim=open("stim.stim","r")
for line in stim:
	lst=line.strip().replace(" ","").split(",")
	variables[lst[1]].update(int(lst[2]))
