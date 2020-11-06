#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

value=input('Enter Container Name :-  ')
image=input('Enter Image Name :-  ')
cmd="sudo docker run -dit --name {} {}".format(value, image)
print(subprocess.getoutput(cmd))

