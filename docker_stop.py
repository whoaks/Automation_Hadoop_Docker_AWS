#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

value=input('Enter name to stop docker container :-  ')
cmd="sudo docker stop {}".format(value)
print(subprocess.getoutput(cmd))

