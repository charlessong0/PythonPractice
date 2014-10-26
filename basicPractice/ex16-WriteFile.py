# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print 'we are going to erase %s' %script
print 'if you do not want that, press control+C'
print ' else just press Enter'

raw_input('want that?')

print 'Operating the file'

target = open(filename, 'w')
target3 = open(filename, 'w')
print 'truncating the file...'
#target3 = open(filename, 'r')
print '-----'
#print target3.read()
target.truncate()
#target4 = open(filename)
#print target4.read()

print ' now please input three lines:'

line1 = raw_input('line1')
line2 = raw_input('line2')
line3 = raw_input('line3')

print 'Now we can write this file!'

target.write(line1)
target3.write('haha123')
target.write("\n")
target.write(line2+"\n")
target.write(line3)

'''
if the file is not closed yet, target2 will read what it looks like as the function truncate finished
'''
target2 = open(filename)
print target2.read()
target.close()
target3.close()
print target2.read()
