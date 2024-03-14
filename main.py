from gate import gate, getVars
import sys

variables=getVars("circuits.cir")
delay=0



print("starting updates")

with open("stim.stim","r" ) as stim:
	for line in stim:
		lst=line.strip().replace(" ","").split(",")
		delay+=variables[lst[1]].update(int(lst[2]))
		print(delay)
