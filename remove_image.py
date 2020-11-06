#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

value=input('Enter image name to remove from local OS :-  ')
cmd="sudo docker rmi {}".format(value)
print(subprocess.getoutput(cmd))

