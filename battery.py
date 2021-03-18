#!/usr/bin/python

import subprocess

process = subprocess.Popen(['acpi','--battery'],stdout=subprocess.PIPE)
stdout = process.communicate()[0].decode()
battery = int(stdout.split()[3][:-2])
process = subprocess.Popen(['acpi','--thermal'],stdout=subprocess.PIPE)
stdout = process.communicate()[0].decode()
thermal = float(stdout.split()[3])
print('<openbox_pipe_menu>')
print('<item label="Battery: {battery}%"/>'.format(battery=battery))
print('<item label="Thermal: {thermal}C"/>'.format(thermal=thermal))
print('</openbox_pipe_menu>')


