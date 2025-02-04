
# The type float

nb=23.2 # "fixed" notation 
print(nb, type(nb))
nb=-67.89 # "fixed" notation
print(nb, type(nb))
nb=-.89 # "fixed" notation
print(nb, type(nb))
nb=.002 # "fixed" notation
print(nb, type(nb))

nb=23.2E+2 # "scientific" notation 
print(nb, type(nb))
nb=.234e-3 # "scientific" notation 
print(nb, type(nb))
nb=2.2E12 # "scientific" notation 
print(nb, type(nb))

nb=float()
print(nb, type(nb))
nb=float("343.6")
print(nb, type(nb))
nb=float(34)
print(nb, type(nb))


# Operators: + - * / ** % //  modules: math,numpy, ...

print(3**2) # 9
print(13/5) # 2.6
print(13//5) # 2
print(13%5) # 3

# float do have a limit: a maximum size
