#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

value=input('Enter name to remove docker Container :-  ')
cmd="sudo docker rm -f {}".format(value)
print(subprocess.getoutput(cmd))
