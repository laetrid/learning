#!/usr/bin/env python

'''
Learning Python
Class#3
I. Create an IP address converter (dotted decimal to binary).  This will be 
similar to what we did in class2 except:
    A. Make the IP address a command-line argument instead of prompting the user
for it.
            ./binary_converter.py 10.88.17.23
    B. Simplify the script logic by using the flow-control statements that we 
learned in this class.
    C. Zero-pad the digits such that the binary output is always 8-binary digits
long.  Strip off the leading '0b' characters.  For example,
        OLD:     0b1010
        NEW:    00001010
    D. Print to standard output using a dotted binary format.  For example,
        IP address          Binary
        10.88.17.23        00001010.01011000.00010001.00010111
    Note, you will probably need to use a 'while' loop and a 'break' statement 
for part C.
        while True:
            ...
            break       # on some condition (exit the while loop)
    Python will execute this loop again and again until the 'break' is encountered. 
'''

from sys import argv

if len(argv) != 2:
  exit("\tYou should pass one argument for this script.\n\tExample: ./test3_1.py <IP address>")

ip_addr = argv[1]
formatter = "%-20s%-60s"
column1 = "IP address"
column2 = "Binary"

octets = ip_addr.split('.')
ip_addr_bin = []

if len(octets) != 4:
  exit("Invalid IP address entered")

for octet in octets:
  octet = bin(int(octet))
  octet = octet[2:]
  octet = "0" * (8 - len(octet)) + octet
  ip_addr_bin.append(octet)

ip_addr_bin = '.'.join(ip_addr_bin)

print "=" * 80
print formatter % (column1, column2)
print formatter % (ip_addr, ip_addr_bin)
print "=" * 80

# The END
