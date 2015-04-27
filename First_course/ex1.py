#!/usr/bin/env python

ipv6_addr = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"
ipv6_parts = ipv6_addr.split(':')
print ""
print "Splitted IPv6 address: %s" % ipv6_parts
print ""
ipv6_join = ":".join(ipv6_parts)
print "Joined IPv6 address is: %s" % ipv6_join.lower()
print ""

# The END
