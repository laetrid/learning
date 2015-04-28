#!/usr/bin/env python

'''
IV. Create a script that checks the validity of an IP address.  The IP address should be supplied on the command line.
    A. Check that the IP address contains 4 octets.
    B. The first octet must be between 1 - 223.
    C. The first octet cannot be 127.
    D. The IP address cannot be in the 169.254.X.X address space.
    E. The last three octets must range between 0 - 255.

    For output, print the IP and whether it is valid or not.
'''

from sys import argv

print ""

if len(argv) != 2:
  exit("\tYou must enter an IP addres as parameter for this script")

octets = argv[1].strip().split('.')

if len(octets) != 4:
  exit("\tYou must enter IP address in decimal form divided by dot")

for octet in octets:
  try:
    int(octet)
  except ValueError:
    exit("\tIP address must contain only digits.")

if (int(octets[0]) < 1) or (int(octets[0]) > 223):
  exit("\tFirst octet in valid IP address must be in range from 1 to 223")

if int(octets[0]) == 127:
  exit("\tValid IP address cannot be in loopback subnet 127.0.0.0/8")

if (int(octets[0] == 169)) and (int(octets[1] == 254)):
  exit("\tValid IP address cannot be in APIPA subnet 169.254.0.0/16")

for i in range(1,4):
  if (int(octets[i]) < 0) or (int(octets[i]) > 255):
    exit("\tLast three octets must be in range between 0 and 255")

ip_addr = '.'.join(octets)
print "IP address %s is valid" % ip_addr
  
# The END
