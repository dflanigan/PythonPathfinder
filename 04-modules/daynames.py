#!/usr/bin/env python 

import datetime

day_names = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


def list_days():
    for day_index in range(len(day_names)):
        print "  %d : %s" % (day_index,day_names[day_index])


def get_day(date):
    day_index = (date.weekday() + 1) % 7
    return day_names[day_index]
    


if __name__ == "__main__":
    list_days()

    today = datetime.date.today()
    print "Today is %s" % (get_day(today))
