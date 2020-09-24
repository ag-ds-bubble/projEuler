"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
from utils import timing_decorator
import numpy as np
import datetime, calendar

@timing_decorator
def weekday_count(fromdate='01-01-1901', todate='31-12-2000'):
  start_date = datetime.datetime.strptime(fromdate, '%d-%m-%Y')
  end_date = datetime.datetime.strptime(todate, '%d-%m-%Y')
  week = {}
  for i in range((end_date - start_date).days):
    ndate = start_date + datetime.timedelta(days=i+1)
    if ndate.day == 1:
        day = calendar.day_name[ndate.weekday()]
        week[day] = week[day] + 1 if day in week else 1
  return week

print(weekday_count())

