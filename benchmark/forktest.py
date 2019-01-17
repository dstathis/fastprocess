#!/usr/bin/python3

import os
import signal

procs = []

outfh = open('/dev/null', 'w')

for i in range(10000):
    pid = os.fork()
    if pid == 0:
        os.dup2(outfh.fileno(), 1)
        os.execvp('echo', ['echo', 'hello', 'world'])
    procs.append(pid)
for proc in procs:
    os.kill(proc, signal.SIGTERM)
