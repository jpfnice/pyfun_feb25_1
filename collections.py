
"""
Collection: 
    list, tuple, set, dict, array, str, ...
    
    Sequences: collections with the concept of "position"
        list, tuple, str, array

"""

# Size of a collection: len()

text="Hello World"          # a str
print(len(text))

alist=[5,6,10,2,-3,2,10]    # a list
print(len(alist))

aset={5,6,10,2,-3,2,10}     # a set
print(len(aset), aset)

# To iterate through a collection we can use a for loop:

for element in text:
    print(element)

total=0
for e in alist:
    #print(e)
    total = total + e
    
print("Total is",total)

print(aset)
for e in aset:
    print(e)

    
# You can for the presence of an element with the operator in:
    
print("H" in text)
print("Z" in text)
print("H" not in text)
print("Z" not in text)
print(5 in alist)
print(10 in aset)
