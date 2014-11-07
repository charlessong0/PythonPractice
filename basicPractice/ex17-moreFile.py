# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, in_file, out_file = argv
print 'Copying from file %s to file %s!' %(in_file, out_file)

indata = (open(in_file)).read()
print 'the input file is %d bytes long' % len(indata)

print "does the output file exist? %r" % exists(out_file)
print 'Now ready! press enter button and continue. To stop, please press control +c'
raw_input()

out = open(out_file, 'w')
out.write(indata)

out.close

