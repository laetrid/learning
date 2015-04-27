#!/usr/bin/env python

column1 = "NETWORK_NUMBER"
column2 = "FIRST_OCTET_BINARY"
column3 = "FIRST_OCTET_HEX"

ip_addr = '88.19.107.0'
formatter = '%-20s%-20s%-20s'
octets = ip_addr.split('.')
a = bin(int(octets[0]))
b = hex(int(octets[0]))

print ""
print formatter % (column1, column2, column3)
print formatter % (ip_addr, a, b)
print ""
