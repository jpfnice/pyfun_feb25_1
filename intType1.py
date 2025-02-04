
# The type int

nb=23 # decimal representation (base 10)
print(nb, type(nb))
nb=-67
print(nb, type(nb))

nb= 0b1001001 # binary representation (base 2)
print(nb, type(nb))
nb= 0o734 # octal representation (base 8)
print(nb, type(nb))
nb= 0x78AB # hexa representation (base 16)
print(nb, type(nb))

nb=int()
print(nb, type(nb))
nb=int("343")
print(nb, type(nb))
nb=int(34.9)
print(nb, type(nb))
nb=int(False)
print(nb, type(nb))
nb=int(True)
print(nb, type(nb))

# Operators: + - * / ** % //  modules: math,numpy, ...

print(3**2) # 9
print(13/5) # 2.6
print(13//5) # 2
print(13%5) # 3

# int have no limits !
