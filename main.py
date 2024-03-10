from circuit import *

sim=open("stim.stim","r")

for line in sim:
	lst=line.strip().split(",")
	print(lst)