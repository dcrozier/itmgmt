<<<<<<< HEAD
#!/usr/bin/python

import re
import subprocess
import time


minions = {}

while True:
    proc = subprocess.Popen(['cat', '/etc/openvpn/openvpn-status.log'], stdout=subprocess.PIPE)
    log = proc.communicate()[0]
    pattern = [
        re.compile(r'(?P<mac_address>[a-f0-9:]{17}),(?P<host_name>[\w]+),(?P<public_ip>[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3})', re.I|re.M),
        re.compile(r'(?P<host_name>[\w]+),(?P<ip_address>[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3})', re.I|re.MULTILINE)
        ]

    for group in re.finditer(pattern[0], log):
        minions[group.group('host_name')] = {
            'mac_address': group.group('mac_address'),
            'public_ip': group.group('public_ip'),
            'host_name': group.group('host_name')
        }

    proc = subprocess.Popen(['cat', '/etc/openvpn/ipp.txt'], stdout=subprocess.PIPE)
    log = proc.communicate()[0]

    for group in re.finditer(pattern[1], log):
        try: minions[group.group('host_name')].update({'private_ip': group.group('ip_address')})
        except KeyError: pass

    print [minions[minion] for minion in minions]
    time.sleep(10)
=======
#!/usr/bin/python

import re
import subprocess
import time

while True:
    proc = subprocess.Popen(['cat', '/etc/openvpn/openvpn-status.log'], stdout=subprocess.PIPE)
    log = proc.communicate()[0]
    pattern = re.compile(r'(?P<mac_address>[a-f0-9:]{17}),(?P<host_name>[\w]+),(?P<public_ip>[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3})', re.I|re.M)
    print [mac.groupdict() for mac in re.finditer(pattern, log)]

    proc = subprocess.Popen(['cat', '/etc/openvpn/ipp.txt'], stdout=subprocess.PIPE)
    log = proc.communicate()[0]
    pattern = re.compile(r'(?P<host_name>[\w]+),(?P<ip_address>[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3})', re.I|re.MULTILINE)
    print [mac.groupdict() for mac in re.finditer(pattern, log)]

    time.sleep(1)
>>>>>>> a784ca2f5f897a81f4b4db13769e5b593e944234
