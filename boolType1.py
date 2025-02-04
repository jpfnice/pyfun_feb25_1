
# The type bool (boolean)

nb=True
print(nb, type(nb))

nb=False
print(nb, type(nb))

nb=10>100
print(nb, type(nb))

nb=bool(12)
print(nb, type(nb))
nb=bool(0)
print(nb, type(nb))

# Operators: > < <= >= == != and or not

print(not ((nb>10 and nb<20) or (nb>40 and nb<60)))