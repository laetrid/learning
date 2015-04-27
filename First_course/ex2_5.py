#!/usr/bin/env python

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

parts = cisco_ios.split(',')[2]
ios_version = parts.split(' Version ')[1]

print ""
print ios_version
print ""

# The END
