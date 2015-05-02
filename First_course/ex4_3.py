#!/usr/bin/env python

'''
III. Create a program that converts the following uptime strings to a time in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name as the key.

During this conversion process, you will have to convert strings to integers.  For these string to integer conversions use try/except to catch any string to integer conversion exceptions.

For example:
int('5') works fine
int('5 years') generates a ValueError exception.

Print the dictionary to standard output.
'''

uptime_in = '''
uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'
'''

uptime_list = uptime_in.split('\n')[1:-1]
result_dic = {}

for line in uptime_list:
  a, b = line[11:-1].split(' uptime is ')
  result_dic[a] = b

for key in result_dic.keys():
  time_list = result_dic[key].split(', ')
  years = 0
  weeks = 0
  days = 0
  hours = 0
  minutes = 0
  for time in time_list:
    try:
      if 'year' in time: years = int(time.split()[0]) * 31556926 
      if 'week' in time: weeks = int(time.split()[0]) * 604800
      if 'day' in time: days = int(time.split()[0]) * 86400
      if 'hour' in time: hours = int(time.split()[0]) * 3600
      if 'minute' in time: minutes = int(time.split()[0]) * 60
    except ValueError:
      print("Error with converting string")
  result_dic[key] = "%-10dsec (%s)" % (years + weeks + days + hours + minutes, result_dic[key])

print ""
print "=" * 70
for key in result_dic.keys():
  print "%-12s:%s" % (key, result_dic[key])
print "=" * 70
print ""

# The END
