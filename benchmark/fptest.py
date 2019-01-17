#!/usr/bin/python3

from fastprocess import Fp

procs = []

for i in range(10000):
    procs.append(Fp(['echo', 'hello', 'world'], stdout=open('/dev/null', 'w')))
