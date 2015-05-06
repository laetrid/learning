#!/usr/bin/env python

'''
Scriot that gets
# Uptime when running config last changed    
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
and 
# Uptime when startup config last saved   
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
compare them and decided whether or not latest changes in running-config are saved in startup-config
'''

# Import Kirk`s module 
from snmp_helper import snmp_get_oid, snmp_extract


# Define variables
device = "1.1.1.1"
community = "*****"
snmp_port = "161"

run_last_change_oid = "1.3.6.1.4.1.9.9.43.1.1.1.0"
start_last_change_oid = "1.3.6.1.4.1.9.9.43.1.1.3.0"
sys_uptime_oid = "1.3.6.1.2.1.1.3.0"

# Define device tuple
a_device = (device, community, snmp_port)

#Query data 
run_last_change = snmp_extract(snmp_get_oid(a_device, run_last_change_oid,))
start_last_change = snmp_extract(snmp_get_oid(a_device, start_last_change_oid,))
sys_uptime = snmp_extract(snmp_get_oid(a_device, sys_uptime_oid,))

#Convert data in integer
if run_last_change.isdigit() and start_last_change.isdigit() and sys_uptime.isdigit():
    run_last_change = int(run_last_change)
    start_last_change = int(start_last_change)
    sys_uptime = int(sys_uptime)
else:
    exit("Error with SNMP response (non digits)")

if start_last_change == 0 and run_last_change > 3000:
    exit("Config was never saved to startup since last reboot, but running-config was changed")

if start_last_change >= run_last_change:
    exit("All right, last changes was saved to startup config")
else:
    dif_time = (sys_uptime - start_last_change) / 100
    exit("Last changes to running config wasn't saved to startup %d seconds already" % dif_time)

# The END
