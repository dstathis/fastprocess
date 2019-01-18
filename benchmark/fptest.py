#!/usr/bin/python3

from fastprocess import FastProcess

procs = []

for i in range(10000):
    procs.append(FastProcess(['echo', 'hello', 'world'], stdout=open('/dev/null', 'w')))
