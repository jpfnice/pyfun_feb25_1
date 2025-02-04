"""
Write a Python script that prompts the user for a number and displays a message that does indicate if the number is odd or even.

Note: do consider 0 has being neither odd nor even.

After having tested a first number, the script should prompt the user for other numbers as long as he or she would like to.

Note: to determine if a number is even you compute the remainder (via the %
operator) of the division of this number by two, if it is zero, the number 
is even.
Unless the number is zero: zero is neither odd nor even

"""

nb=input("Please enter a number: ")
nb=int(nb)
    
if nb == 0:
    print(nb,"is neither even nor odd !")
elif nb % 2 == 0:
    print(nb,"is even")
else:
    print(nb,"is odd")

