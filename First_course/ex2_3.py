#!/usr/bin/env python
#
# IP address decimal to binary convertor

ip_addr = raw_input("Enter an IP address: ")
print "\n" * 5
print "=" * 80

formatter = "%-20s%-20s%-20s%-20s"
octets = ip_addr.split('.')

column1 = 'first_octet'
column2 = 'second_octet'
column3 = 'third_octet'
column4 = 'fourth_octet'

octets[0] = int(octets[0])
octets[1] = int(octets[1])
octets[2] = int(octets[2])
octets[3] = int(octets[3])

print formatter % (column1, column2, column3, column4)
print formatter % (bin(octets[0]), bin(octets[1]), bin(octets[2]), bin(octets[3]))
print "=" * 80
print formatter % (column1, column2, column3, column4)
print formatter % (hex(octets[0]), hex(octets[1]), hex(octets[2]), hex(octets[3]))
print "\n" * 5
# The END
