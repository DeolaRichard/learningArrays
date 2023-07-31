from array import *

vals = array("i", [5, 9, 8, 4, 2, 9, 3, 0])
# getting the address and length of the array
print(vals.buffer_info())

# making a copy of the previous array and then doubling each value
newArr = array(vals.typecode, (a*a for a in vals))
# reversing the sequence of an array
vals.reverse()
for i in range(len(vals)):
    print(vals[i])
print(newArr)
