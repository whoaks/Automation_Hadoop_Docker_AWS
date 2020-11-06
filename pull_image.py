#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

value=input('Enter Image name to pull it from docker hub :-  ')
cmd="sudo docker pull {}".format(value)
print(subprocess.getoutput(cmd))
