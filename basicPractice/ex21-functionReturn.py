# -*- coding: utf-8 -*-
from sys import argv

script, var1, var2 = argv
def add_two_numbers(a, b):
	print "returning the sum of two numbers"
	return a+b

print add_two_numbers(int(var1),int(var2))
#print add_two_numbers(var1,var2)
