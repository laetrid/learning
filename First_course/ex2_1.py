#!/usr/bin/env python

ip_addr = raw_input('Enter the IP address >')

octets = ip_addr.split('.')
octets = octets[0:3]
octets.append('0')

net_addr = ".".join(octets)
print ""
print "The network address is %s/24" % net_addr
print ""

# The END
