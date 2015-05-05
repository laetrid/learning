#!/usr/bin/env python

'''
5. Write a program that prompts a user for an IP address, then checks if the IP address is valid, and then converts the IP address to binary (dotted decimal format). Re-use the functions created in exercises 3 and 4 ('import' the functions into your new program).
'''

# Import functiosn - ip check, ip to bin and bin padding
from ex6_3 import ip_checker
from ex6_4 import ip2bin, bin_padding

ip_valid = False

while not ip_valid:
    ip_addr = raw_input('Please enter an IP address: ')
    ip_valid = ip_checker(ip_addr)

ip_addr_bin = ip2bin(ip_addr)
bin_padding(ip_addr_bin)

print ""
print "The IP address: %s is valid." % ip_addr
print "In binary it is: %s." % '.'.join(ip_addr_bin)
print ""

# The END
