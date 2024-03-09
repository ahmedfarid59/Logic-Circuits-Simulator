from component import *

file=open("lib.lib","r")

for l in file:
	lst=l.strip().split(",")
	print(lst)

