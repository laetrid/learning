#!/usr/bin/env python

'''
3a.Convert the IP address validation code (Class4, exercise1) into a function, take one variable 'ip_address' and return either True or False (depending on whether 'ip_address' is a valid IP). Only include IP address checking in the function--no prompting for input, no printing to standard output.


3b. Import this IP address validation function into the Python interpreter shell and test it (use both 'import x' and 'from x import y').
'''


def ip_checker(ip_addr):

    def octet_val(octets):
        i = 0
        for octet in octets:
            if (int(octet) >= 0) and (int(octet) < 256): i += 1
        return i

    octets = ip_addr.split('.')
    if len(octets) != 4:
        print "\t(1-split)Invalid IP address, try again"
        return
    if octets[0].isdigit() + octets[1].isdigit() + octets[2].isdigit() + octets[3].isdigit() != 4:
        print "\t(2-is digit) Invalid IP address, try again"
        return
    if (int(octets[0]) < 1) or (int(octets[0]) > 223):
        print "\t(3-first octet) Invalid IP address, try again"
        return
    if int(octets[0]) == 127:
        print "\t(4-loopback) Invalid IP address, try again"
        return
    if (int(octets[0]) == 169) and (int(octets[1]) == 254):
        print "\t (5 - APIPA) Invalid IP address, try again"
        return
    if octet_val(octets) != 4:
        print "\t (6 - octets not in range 0-255) Invalid IP address, try again"
        return
    # If func didn't return to main before then IP is all right and I can returt True
    return True

if_valid = False

while not if_valid:
    print ""
    ip_addr = raw_input('Please enter an IP address: ')
    if_valid = ip_checker(ip_addr)

print ""
print "IP address: %s is valid" % ip_addr
print "Goodbye!"
print ""

# The END
