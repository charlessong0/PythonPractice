# -*- coding: utf-8 -*-
from sys import argv

print "now we should have more practice.."
print "first try some \'slash\' and backslash \\. I\'d like to show something about that"

test_words = """secondely, 
I would like to try some
\t\'\\t\' and some other stuff like \n and more!
is this enough for me?\n\fI think so"""

line = "================"

print line
print test_words
print line

#now here is a function for Python
def test_function(input_number):
	print "haha123"
	my = input_number*10
	you = my+1
	he = you/5
	return my, you, he

score1 = 0
score2 =0
score3=0

print "the argv is", argv[1]
if argv[1] == "1":
	score1, score2, score3 = test_function(100)
	print 1231231
elif argv[1] == "2":
	array = test_function(9)
	score1 = array[0]
	score2 = array[1]
	score3 = array[2]
	print 233333

#now let's test printing with variables
print "my score here is %s." %score1
print "the others' socres are %d and %r, again, my score is %s" %(score1,score2,score3)

