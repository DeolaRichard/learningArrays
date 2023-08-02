from array import *

vals = array("i", [5, 9, 8, 4, 2, 9, 3, 0])
# to sort the array in ascending order without modifying the initial array
sorted_vals = sorted(vals)
print("Sorted array: ", sorted_vals)

# getting the address and length of the array
print(vals.buffer_info())

# making a copy of the previous array and then doubling each value
newArr = array(vals.typecode, (a * a for a in vals))

# reversing the sequence of an array
vals.reverse()
for i in range(len(vals)):
    print(vals[i])
print(newArr)

# getting data inputs from user & storing the data in an array
arr = array('i', [])

a = int(input("Hey, how many data do you want to input?: "))

for i in range(a):
    x = int(input("Input the Next Value: "))
    arr.append(x)

print(arr)


# write a code to find a factorial of a given number
def factorial(n):
    if n < 0:
        return "Factorial not available for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for b in range(2, n + 1):
            result *= b
        return result


# Test the function with some examples
print(factorial(10))
print(factorial(3))
