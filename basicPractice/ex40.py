# -*- coding: utf-8 -*-
# this is an exercise for dictionary, module and class

# test on dictionary
break_line = "=============================="
dic = {"test":123, "input":"haha123"}
print dic.get("test")
print dic["test"]
print dic.get('input')

print break_line
# test on modules
# ex25.py - test1(number)
import ex25
print ex25.test1(1)
print ex25.test1(11)
ex25.numbers = 999
print ex25.numbers

import ex25
print ex25.numbers

print break_line
# test on class!
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_a_song(self):
        for lines in self.lyrics:
            print lines

my_lyrics = ["you are my sunshine", "my only sunshine"]
first_class = Song(my_lyrics)
#first_class = Song(["you are here","haha123"])
first_class.sing_a_song()

# another test on class
print break_line

class AnotherSong(object):
    def some_thing(test):
        print "haha123"
test_on_class = AnotherSong()
test_on_class.some_thing()

