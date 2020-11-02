#!/usr/bin/env python
# bsp01_WHILE.py	
#-----------------------------------
# 19.09.2018 by OJ
#----------------------------------- 

#---- Variablen ----
i = 0
#print("Zahl  2.Pot  3.Pot");
while(i<=9):
	#print("Zahl %02d 2.Pot %03d 3.Pot %04d" %( i , i**2, i**3) );	
	print("Zahl {0:02d} 2.Pot {1:03d} 3.Pot {2:04d}".format( i , i**2, i**3) );	
	i+=1; # i++ gibt es nicht!

print("Schleife zu Ende")




