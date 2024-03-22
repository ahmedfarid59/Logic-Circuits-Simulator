from modules.gate import  getVars
import sys
#The main file
#reading the gates file (.cir)
variables=getVars("testCases\\circuit5\\circuit5.cir")

print("starting updates")
# reading the stim file and updating the variables after removing the whitespaces and extra line breaks and normalizing the cases
with open("modules\\stim.stim","r" ) as stim:
	for line in stim:

		lst=line.strip().replace(" ","").upper().split(",")
		d=int(lst[0])
		variables[lst[1]].update(int(lst[2]),d)