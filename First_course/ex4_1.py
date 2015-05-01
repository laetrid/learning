#!/usr/bin/env python

'''
Prompt a user to input an IP address.  Re-using some of the code from class3,
exercise4--determine if the IP address is valid.  Continue prompting the user
to re-input an IP address until a valid IP address is input.
'''

# IP address checker

def octet_val(octets):
  i = 0
  for octet in octets:
    if (int(octet) >= 0) and (int(octet) < 256): i += 1
  return i

result = True
l_result = True

while result == True:
  print ""
  ip_addr = raw_input("Please enter an IPv4 address: ")
  octets = ip_addr.split('.')
  while l_result:
    if len(octets) != 4:
      print "\t(1-split)Invalid IP address, try again"
      break
    if octets[0].isdigit() + octets[1].isdigit() + octets[2].isdigit() + octets[3].isdigit() != 4:
      print "\t(2-is digit) Invalid IP address, try again"
      break
    if (int(octets[0]) < 1) or (int(octets[0]) > 223):
      print "\t(3-first octet) Invalid IP address, try again"
      break
    if int(octets[0]) == 127:
      print "\t(4-loopback) Invalid IP address, try again"
      break
    if (int(octets[0]) == 169) and (int(octets[1]) == 254):
      print "\t (5 - APIPA) Invalid IP address, try again"
      break
    if octet_val(octets) != 4:
      print "\t (6 - octets not in range 0-255) Invalid IP address, try again"
      break
    result = False
    break
    
print ""
print "IPv4 address: %s is valid" % ip_addr
print "The END"
   
# The END
