
"""
Collection: 
    list, tuple, set, dict, array, str, ...
    
    Sequences: collections with the concept of "position"
        list, tuple, str, array

"""

# first element of a sequence: [0]

text="Hello World" # a str is a "immutable" sequence
print(text[0])
print(text[1])


alist=[5,6,10,2,-3,2,10] # a list is a "mutable" sequence
print(alist)
print(alist[0])
alist[0]=34
print(alist)

# last element of a sequence: [-1]

text="Hello World"
print(text[-1])
print(text[len(text)-1])
print(text)

alist=[5,6,10,2,-3,2,10]
print(alist[-2])
print(alist)
alist[1]=7
print(alist)

# slice of a sequence: [start:stop] or [start:stop:inc]

text="Hello World"
print(text[2:7]) # 2,3,4,5,6
print(text[2:7:2]) # 2,4,6
print(text[:7]) # 0,1,2,..,6
print(text[3:]) # 3,4,5,6...

alist=[5,6,10,2,-3,2,10]
print(alist[1:6])
print(alist[1:6:3])

# duplicating elements with *

text="AB"*10
print(text)
text="-"*80
print(text)

alist=[0]*100
print(alist)

# concatenating elements with +

text="ABC" + "DEF"
print(text)


alist=[3,4,5] + [10,11]
print(alist)





