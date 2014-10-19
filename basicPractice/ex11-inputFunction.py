# -*- coding: utf-8 -*-

print 'please input age'
age = raw_input()
print 'please input name'
name = raw_input()
print 'please input thisyear'
thisyear = raw_input()
'''
print 'please input test message'
test = input()
'''
print ' please input test number'
testNum = input()


print 'I am %s years old' %age
print 'and my name is %r' %name 
print 'my birthyear is %r and my age is %r' %(int(thisyear)-int(age), age)
#print 'test', test
print 'test number %r' %testNum
