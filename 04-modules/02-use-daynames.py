#! /usr/bin/env python

import datetime
import daynames

print "calling list_days:"
daynames.list_days()

today = datetime.date.today()
print "Today is %s" % (daynames.get_day(today))

one_day = datetime.timedelta(days=1)
tomorrow = today + one_day
print "Tomorrow is %s" % (daynames.get_day(tomorrow))

