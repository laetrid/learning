#!/usr/bin/env python

'''
4. Create a function using your dotted decimal to binary conversion code from Class3, exercise1. In the function--do not prompt for input and do not print to standard output. The function should take one variable 'ip_address' and should return the IP address in dotted binary format always padded to eight binary digits (for example, 00001010.01011000.00010001.00010111). You might want to create other functions as well (for example, the zero-padding to eight binary digits).
'''

# Convert IP to binary with functions

# First convert func
def ip2bin(ip_addr):
    ip_addr_bin = []    
    octets = ip_addr.split('.')
    for octet in octets:
        octet = int(octet)
        ip_addr_bin.append(bin(octet)[2:])
    return ip_addr_bin

# Second padding adding function
def bin_padding(ip_addr_bin):
    for i, octet in enumerate(ip_addr_bin):
        ip_addr_bin[i] = "0" * (8 - len(octet)) + octet
        

print ""
ip_addr = raw_input('Please, enter an IP address: ')
ip_addr_bin = ip2bin(ip_addr)
bin_padding(ip_addr_bin)
print '.'.join(ip_addr_bin)

# The END
