#! /usr/bin/env python

import sys

print "sys.path type is: "
print type(sys.path)
print 
print "sys.path is: "
paths =  sys.path
for path_index in range(len(paths)):
    print "   %s" % paths[path_index]


