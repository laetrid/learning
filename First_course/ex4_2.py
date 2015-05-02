
#!/usr/bin/env python

'''
Parse the below 'show version' data and obtain the following items (vendor, 
model, os_version, uptime, and serial_number).  Try to make your string parsing
generic i.e. it would work for other Cisco IOS devices. 
The following are reasonable strings to look for:
'Cisco IOS Software' for vendor and os_version
'bytes of memory' for model
'Processor board ID' for serial_number
' uptime is ' for uptime
Store these variables (vendor, model, os_version, uptime, and serial_number) in 
a dictionary.  Print the dictionary to standard output when done.
Note, "Cisco IOS Software...Version 15.0(1)M4...(fc1)" is one line.

file with sh ver is ex4_2.txt
'''


from sys import argv

filename = argv[1]

sh_ver = open(filename).read()

sh_ver_lines = sh_ver.split('\n')

result_lines = []

for line in sh_ver_lines:
  if line.find('Cisco IOS Software') != -1: line1 = line.split(', ')
  if line.find('bytes of memory') != -1: line2 = line.split('(')
  if line.find('Processor board ID') != -1: line3 = line.split()
  if line.find('uptime is') != -1: line4 = line.split('is ')

result_dic = {}
 
result_dic['vendor'] = line1[0].split()[0]
result_dic['os_version'] = line1[2].split()[1]
result_dic['model'] = line2[0].split()[1]
result_dic['serial_number'] = line3[3]
result_dic['uptime'] = line4[1]

print "=" * 60
for key in result_dic.keys():
  print "%-15s%-45s" % (key, result_dic[key])
print "=" * 60
print ""
