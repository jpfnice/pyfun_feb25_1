"""
    input() -> str
    float(argument) -> float
    int(argument) -> int
    
"""
import math

nb=input("Enter a numeric value: ")
print("Nb is", nb, type(nb))

nb=int(nb)

result=math.sqrt(nb)
print(result)

