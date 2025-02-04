"""

If condition is True, bloc 1 is executed:

if condition:
    bloc 1

If condition is True, bloc 1 is executed otherwise bloc 2 is executed:
    
if condition:
    bloc 1
else:
    bloc 2
      
"""
nb = -8

"""
Operators that return a bool result:
    
< > <= >= == !=

and or not

"""
if nb > 100:
    print("Nb is > 100")
elif nb <= 100 and nb > 0:
    print("Nb is in ]0,100]")
elif nb <= 0 and nb > -10:
    print("Nb is in ]-5,0]")
else:
    print("Else part")
    


