#!/usr/bin/env python

'''
1. Create a function that returns the multiplication product of three parameters--x, y, and z. z should have a default value of 1.
    a. Call the function with all positional arguments.
    b. Call the function with all named arguments.  
    c. Call the function with a mix of positional and named arguments.
    d. Call the function with only two arguments and use the default value for z.
'''

# Func defenition
def multi_three(x, y, z = 30):
    return x * y * z

# Main prigram

a = 10
b = 20
c = 30

multipl = multi_three(10, 20, 30)
print "A. Call the function with all positional arguments. ==> %d" % multipl

multipl = multi_three(a, b, c)
print "B. Call the function with all named arguments. ==> %d" % multipl

multipl = multi_three(a, z = c, y = 20)
print "C. Call the function with a mix of positional and named arguments. ==> %d" % multipl

multipl = multi_three(a, b)
print "D. Call the function with only two arguments and use the default value for z. ==> %d" % multipl

# The END
