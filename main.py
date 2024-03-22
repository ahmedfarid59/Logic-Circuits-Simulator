from modules.gate import  getVars
import sys

variables=getVars("testCases\\circuit5\\circuit5.cir")

print("starting updates")

with open("modules\\stim.stim","r" ) as stim:
	for line in stim:
		lst=line.strip().replace(" ","").upper().split(",")
		d=int(lst[0])
		variables[lst[1]].update(int(lst[2]),d)