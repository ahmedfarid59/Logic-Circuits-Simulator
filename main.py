from modules.gate import  getVars
import matplotlib
from matplotlib import pyplot as pt 

import sys

#The main file
#reading the gates file (.cir)
variables=getVars("testCases\\circuit5\\circuit5.cir")

# reading the stim file and updating the variables after removing the whitespaces and extra line breaks and normalizing the cases
with open("modules\\stim.stim","r" ) as stim:
	for line in stim:
		lst=line.strip().replace(" ","").upper().split(",")
		t=int(lst[0])
		variables[lst[1]].update(int(lst[2]),t,0)

#getting predefined list of colors to distinguish each line
colormap = matplotlib.colormaps.get_cmap('viridis')
# Generating a list of 50 distinct colors with high contrast
colorList = [colormap(i / 50)[:3] for i in range(50)]

#ploting every curve  one per variable 
for i, (name, var) in enumerate(variables.items()):
    pt.plot(var.x, var.y, label=name, color=colorList[i])
pt.show()