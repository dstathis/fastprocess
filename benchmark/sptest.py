#!/usr/bin/python3

import subprocess

procs = []

for i in range(10000):
    procs.append(subprocess.Popen(['echo', 'hello', 'world'], stdout=open('/dev/null', 'w')))
