#!/usr/bin/env python

'''
1. Using SNMPv3 create a script that detects changes to the running configuration. If the running configuration is changed, then send an email notification to yourself identifying the router that changed and the time that it changed.

Note, the running configuration of pynet-rtr2 is changing every 15 minutes (roughly at 0, 15, 30, and 45 minutes after the hour).  This will allow you to test your script in the lab environment. I will continue to do this for at least the next week.

In this exercise, you will possibly need to save data to an external file. One way you can accomplish this is by using a pickle file, see:  
    http://youtu.be/ZJOJjyhhEvM  

A pickle file lets you save native Python data structures (dictionaries, lists, objects) directly to a file.

Bonus challenge: instead of saving your data in a pickle file, save the data using either a YAML or a JSON file. YAML and JSON are data formats that are both human readable and parseable by computers.

For information on reading/writing YAML and JSON using Python see:
    http://martin-thoma.com/configuration-files-in-python/

Additionally, my alternate solution supports pickle, YAML, or JSON depending on the name of the file (.pkl, .yml, or .json).

(Config options in local ex2_1.json file)
'''

# Import json for load/savedata in file in json format
# Import time to take now time in epoch (seconds)
# Import os.path to check if file with old data present
# Import datetime to convert time in seconds in DD-MM-YYYY HH:MM:SS form
# Import snmp_helper to get SNMPv3 data from devices
# Import smtplib for sending emails
# Import email.mime.text to convert message in MIME format
import json, time, os.path, datetime, smtplib
from snmp_helper import snmp_get_oid_v3, snmp_extract
from email.mime.text import MIMEText

# Function Get snmp values
def get_snmp_conf_time(snmp_conf, snmp_oids):
    snmp_tmp = {}
    for oid_name, oid in snmp_oids:
        snmp_device = (snmp_conf['ip_addr'], int(snmp_conf['snmp_port']))
        snmp_user = (snmp_conf['snmp_user'], snmp_conf['snmp_auth_key'], snmp_conf['snmp_encrypt_key'])
        snmp_tmp[oid_name] = int(snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, oid))) / 100
    return snmp_tmp # Return dictionary with uptime and run|start time

# This func takes dict with config and string of message body.
def send_mail(email, message):
    message = '''
    Hello!

    %s

    Redards,
    ex2_1.py
    ''' % message
    message = MIMEText(message)
    message['Subject'] = 'Change in config occure.'
    message['From'] = email['from']
    message['To'] = email['to']
    
    # Create SMTP connection object to var from dic
    smtp_conn = smtplib.SMTP(email['server'])

    # Send an email
    smtp_conn.sendmail(email['from'], email['to'], message.as_string())

    # Gracefully closing SMTP connection
    smtp_conn.quit()

# Start main program
def main():
    # Set SNMP oids 
    snmp_oids = (
        ('sysUptime', '1.3.6.1.2.1.1.3.0'),
        ('ccmHistoryRunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0'),
        ('ccmHistoryStartupLastChanged', '1.3.6.1.4.1.9.9.43.1.1.3.0'),
    )
    
    # Define variables
    snmp_time = {}
    snmp_time_old = {}
    cfg_changed = False    
    now_time = int(round(time.time()))
    
    # Read config from file
    with open('ex2_1.json') as json_conf_file:
        conf = json.load(json_conf_file)

    snmp = conf['network_devices']
    email = conf['email_opt']

    # Check if file with previous results exist and if it is, reading from it
    if os.path.isfile('ex2_1_results.json'):
        with open('ex2_1_results.json') as json_file:
            snmp_time_old = json.load(json_file)

    # Get snmp data
    for host in snmp.keys():
        snmp_time[host] = get_snmp_conf_time(snmp[host], snmp_oids)

    # Check whether or not running config was changed
    if snmp_time_old:
        for key in snmp_time.keys():
            if snmp_time[key]['sysUptime'] > snmp_time_old[key]['sysUptime'] and snmp_time[key]['ccmHistoryRunningLastChanged'] > snmp_time_old[key]['ccmHistoryRunningLastChanged']:
                # If it did change, calculate and print time of change, plus send a mail
                date = now_time - snmp_time[key]['sysUptime'] + snmp_time[key]['ccmHistoryRunningLastChanged']
                date = datetime.datetime.fromtimestamp(date).strftime('%d-%m-%Y %H:%M:%S')
                message = "Config on %s was changed at %s." % (key, date)
                print message + "Mail was send"
                send_mail(email, message)       
            else:
                # If it didn`t change, calculate and print last time of change. 
                date = now_time - snmp_time[key]['sysUptime'] + snmp_time[key]['ccmHistoryRunningLastChanged']
                date = datetime.datetime.fromtimestamp(date).strftime('%d-%m-%Y %H:%M:%S')
                print "Config on %s don't changed. Last change: %s." % (key, date)
            print ""
    print ""

    #Finaly replace old values in the file
    with open('ex2_1_results.json', 'w') as json_result_file:
        json.dump(snmp_time, json_result_file, indent = 4, separators=(',', ':'))

if __name__ == '__main__':
    main()

# The END
