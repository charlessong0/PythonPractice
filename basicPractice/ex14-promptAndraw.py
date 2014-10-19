# -*- coding: utf-8 -*-
from sys import argv

script, name = argv
prompt = '>'

print name
print "your name"
name = raw_input(prompt)
print name
like = raw_input(prompt)
print 'test %r' %bool(like)

