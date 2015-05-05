#!/usr/bin/env python

DEBUG = False
# CDP data parser

# All data imports from test5_base.py
import test5_base
from sys import argv

if len(argv) != 1 and argv[1] == '-d': DEBUG = True

# Make list of show cdp neighbor detail commands from test5_base

sh_cdp_detail = []

for line in dir(test5_base):
  if 'cdp' in line and 'detail' in line: sh_cdp_detail.append('test5_base.' + line)

if DEBUG:
  print "*" * 40
  print sh_cdp_detail
  print "*" * 40

# Create formatter for program output
formatter = "|%-9s|%-16s|%-6s|%-16s|%-12s|%-20s"
formatter_dic = "|%(ip)-16s|%(vendor)-6s|%(model)-16s|%(device_type)-12s|%(neighbors)-20s"
column1 = "Hostname"
column2 = "IP address"
column3 = "Vendor"
column4 = "Model"
column5 = "Device Type"  
column6 = "Neighbors"
# Start scrapping CDP

network_devices = {}
tmp_dev = []

for sh in sh_cdp_detail:    # start evaluate
  for line in eval(sh).split('\n'): # evaluate line by line all sh cdp neigh det
    if 'Device ID' in line:
      a = line.split(': ')[1] # tmp for first key in dict
      network_devices[a] = {}
    if 'IP address' in line:
      network_devices[a]['ip'] = line.split(': ')[1]
    if 'Platform: ' in line:
      network_devices[a]['model'] = line.split(', ')[0].split(': ')[1].split()[1]
      network_devices[a]['device_type'] = line.split(', ')[1].split(': ')[1].split()[0]
      network_devices[a]['vendor'] = line.split(', ')[0].split(': ')[1].split()[0]
for sh in sh_cdp_detail:
  for line in eval(sh).split('\n'):
    if '>' in line:
      a = line.split('>')[0]
      network_devices[a]['neighbors'] = []
    if 'Device ID' in line:
      network_devices[a]['neighbors'].append(line.split(': ')[1])

print ""
print "=" * 80
print formatter % (column1, column2, column3, column4, column5, column6)
for key in network_devices.keys():
  print "|%-8s" % key, 
  print formatter_dic % network_devices[key]
print "=" * 80
print ""

# The END
