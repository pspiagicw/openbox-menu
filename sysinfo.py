#!/bin/python
import os
import xml.etree.ElementTree as ET

uptime = None
kernel = None
load = None
mem = None
theme = None

with open('/proc/uptime') as file:
    line = file.read().split()[0]
    uptime = float(line) // 3600 
with open('/proc/version') as file:
    line = file.read().split()[2]
    kernel = line
with open('/proc/meminfo') as file:
    total = None
    lines = file.readlines()
    memtotal = int(lines[0].split()[1])
    memfree = int(lines[2].split()[1])
    mem = int(float((memtotal - memfree)/memtotal) * 100)
    
openbox_config = '~/.config/openbox/rc.xml'
xmlconfig = ET.parse(os.path.expanduser(openbox_config))
load = os.getloadavg()

root = xmlconfig.getroot()
theme = root[3][0].text
print('<openbox_pipe_menu>')
print('<item label="System Info"/>')
print('<seperator/>')
print('<item label="UPTIME: {}"/>'.format(uptime))
print('<item label="KERNEL: {}"/>'.format(kernel))
print('<item label="LOAD: {}"/>'.format(load))
print('<item label="MEM: {}%"/>'.format(mem))
print('<item label="THEME: {}"/>'.format(theme))
print('</openbox_pipe_menu>')
