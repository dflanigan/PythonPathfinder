#!/usr/bin/env python


def integer_math(a,b):
    print ""
    c = a+b
    print " %2d + %2d = %2d ,  result type is %s" % (a,b,c,type(c))
    c = a-b
    print " %2d - %2d = %2d ,  result type is %s" % (a,b,c,type(c))
    c = a*b
    print " %2d * %2d = %2d ,  result type is %s" % (a,b,c,type(c))
    c = a/b
    print " %2d / %2d = %2d ,  result type is %s" % (a,b,c,type(c))
    print ""

integer_math(9,3)
integer_math(7,2)
integer_math(11,4)





