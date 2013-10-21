#! /usr/bin/env python


import daynames

dayname_defines = dir(daynames)

for index in range(len(dayname_defines)):
    print dayname_defines[index]

