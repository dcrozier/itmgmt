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
