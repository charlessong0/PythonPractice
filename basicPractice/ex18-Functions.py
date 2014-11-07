# -*- coding: utf-8 -*-

def print_three(*three):
	arg1, arg2, arg3 = three
	print 'arg1 is %r, and arg2 is %r, meanwhile arg3 is %r' %(arg1, arg2, arg3)

print_three('test1', "test2",123)
