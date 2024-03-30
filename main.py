from modules.gate import  getVars
from matplotlib import pyplot as pt 

from sys import argv, exit

#The main file

if len(argv)==4:
	stim=argv[3]
	cir=argv[2]
else:
	print("invalid input")
	exit()

#reading the gates file (.cir)
variables=getVars(cir)

# reading the stim file and updating the variables after removing the whitespaces and extra line breaks and normalizing the cases
with open(stim,"r" ) as stim:
	for line in stim:
		lst=line.strip().replace(" ","").upper().split(",")
		t=int(lst[0])
		variables[lst[1]].update(int(lst[2]),t,0)

#ploting every curve  one per variable 
for i, (name, var) in enumerate(variables.items()):
    pt.plot(var.x, var.y, label=name)
pt.show()