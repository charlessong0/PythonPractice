# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv
current = open(input_file)
print current.read()

print current.readline(),123

current.seek(0)

print current.readline()

current.close()
