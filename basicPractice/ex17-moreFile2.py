# -*- coding:utf-8 -*-
from sys import argv
from os.path import exists

script, in_file, out_file = argv

print "copying from %s to %s" % (in_file, out_file)
infile = open(in_file)
indata = infile.read()

print "dose the outfile exist? - %r" % exists(out_file)
print "ready, print Enter to continue, print ctr+c to abort"

outfile = open(out_file, "w")
outfile.write(indata)

infile.close()
outfile.close()



