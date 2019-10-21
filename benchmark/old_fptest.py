#!/usr/bin/python3

from fastprocess import FastProcess, OldFastProcess

procs = []

for i in range(10000):
    procs.append(OldFastProcess(['echo', 'hello', 'world'], stdout=open('/dev/null', 'w')))
