# -*- coding: utf-8 -*-

formatter = "%r, %r, %r, %r"

print formatter %('test', 1, False, '1')
print formatter %(formatter, formatter, formatter, formatter)
