# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv
prompt = '>'
test = open(filename)
print test.read()

print 'read again!'
filename = raw_input('file again'+prompt)
test = open(filename)
print test.read()
