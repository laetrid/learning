#!/usr/bin/env python

# Scrypt that gets a SNMP oid

# Import Kyrk`s functions
from snmp_helper import snmp_get_oid, snmp_extract

# Define variables
Device = "1.1.1.1"
Community = "******"
SNMP_port = "161"
OID = "1.3.6.1.2.1.1.5.0"
# Define device tuple
a_device = (Device, Community, SNMP_port)

#Now fun begins
#Query data first
snmp_data = snmp_get_oid(a_device, OID,)

#Convert result data in human readable format
output = snmp_extract(snmp_data)

#And finaly print the result
print output

# The end
