#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

value=input('Enter docker container name to start it :-  ')
cmd="sudo docker start {}".format(value)
print(subprocess.getoutput(cmd))

