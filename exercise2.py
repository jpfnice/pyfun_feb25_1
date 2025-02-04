
"""
Write a Python script that prompts the user for several numbers (when the user enter the string "stop", the script stop asking for numbers).

The numbers entered are stored into a list one after the other.

(Within a loop you prompt the users for numbers using the input() function. Each time a new value is given yoiu append it to a list initialy empty)

After having retrieved all the numbers, print the list.

The script will then compute and print the minimum, the maximum and the mean of the different numbers present in the list.

You can also compute the "truncated mean" of the elements present into the list, i.e. the mean of all elements except the smallest and largest elements:
    If the original list is:
        [1,2,3,1,2,5,1,5,6,2,6]
    The truncated mean will take into account only these elements:
        [2,3,2,5,1,5,2]
        
"""

numbers=[]   # Creation of an empty list <=> numbers=list()

# Step 1:
while True:
    answer=input("Enter an int or 'stop': ")
    if answer=='stop':
        break
    else:
        answer=int(answer)
        numbers.append(answer)

print(numbers)