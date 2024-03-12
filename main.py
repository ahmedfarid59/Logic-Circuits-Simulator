from components import component , getComponents
from variable import variable , variables
from gate import gate
import sys

components=getComponents("lib.lib")
delay=0

with open("circuits.cir","r") as cir:
	for line in cir:
		lst=line.strip().replace(" ","").split(",")
		vn=lst[2]
		if vn not in variables:
			variables[vn]=variable(vn,0)
			print(vn ,"wire was created")
		g=gate(lst[0],components[lst[1]],variables[vn],*[variables[x].state for x in lst[3:]])
		g.refresh()
		for v in lst[3:]:
			variables[v].gates.append(g)
print("starting updates")

with open("stim.stim","r" ) as stim:
	with open("output.sim","w") as sim:
		for line in stim:
		lst=line.strip().replace(" ","").split(",")
			variables[lst[1]].update(int(lst[2]))
