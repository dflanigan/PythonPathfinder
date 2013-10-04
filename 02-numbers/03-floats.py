#! /usr/bin/env python

def show_float(value):
    print ""
    print "value: ",value
    print "formated: %5.2f" % (value)

a = 5.4
b = 8.9
show_float(a)
show_float(b)

c = 7.0 / 3.0
show_float(c)

d = 7.0 / 3
show_float(d)

