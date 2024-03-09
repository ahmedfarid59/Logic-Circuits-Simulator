from component import *

file=open("lib.lib","r")
inputs=components=[]

for l in file:
	lst=l.strip().split(",")
	components.append(component(lst[0],int(lst[1]),lst[2],int(lst[3])))
	print(lst)

