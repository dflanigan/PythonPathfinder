#! /usr/bin/env python

print "\nIntegers"
a = 1
b = 2
print "intergers ",a,b

print "\nOct"
a = 017
b = 025
c = 0100
format = "%d in oct is %o"
print format % (a,a)
print format % (b,b)
print format % (c,c)

print "\nHex"
a = 0xF
b = 0x10
c = 0x80
d = 0xC01
format = "%d in hex is %x or %X"
print format % (a,a,a)
print format % (b,b,b)
print format % (c,c,c)
print format % (d,d,d)




