#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

value=input('Enter Container name to Inspect :-  ')
cmd="sudo docker inspect {}".format(value)
print(subprocess.getoutput(cmd))

