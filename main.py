from gate import  getVars
import sys

variables=getVars("circuit1.cir")

print("starting updates")

with open("stim.stim","r" ) as stim:
	for line in stim:
		lst=line.strip().replace(" ","").split(",")
		d=int(lst[0])
		variables[lst[1]].update(int(lst[2]),d)