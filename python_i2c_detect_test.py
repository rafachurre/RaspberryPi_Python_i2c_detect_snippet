import os
import subprocess
import re

p = subprocess.Popen(['i2cdetect', '-y','0'],stdout=subprocess.PIPE,)
#cmdout = str(p.communicate())

devices = []

for i in range(0,9):
  line = str(p.stdout.readline())

  for match in re.finditer("[0-9][0-9]:.*[0-9][0-9]", line):
    word = line.split(":")[1].split()
    for device in word:
    	if device != "--":
	   devices.append(device)

print devices
