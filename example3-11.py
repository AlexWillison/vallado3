'''
Example 3.11

Companion code for Fundamentals of Astrodynamics and Applications 2007
By David Vallado

Author:
Alex Willison
aawillison@gmail.com
'''

# required imports
from numpy import array
from timeconversions import ymd2doy
from timeconversions import doy2ymd

# first ymd (from Vallado example)
yr1 = 1992
mo1 = 5
day1 = 8

# second ymd (first date +1 day)
yr2 = 1992
mo2 = 5
day2 = 9

# arrange ymd in column vectors
ymd = array(([yr1, yr2], [mo1, mo2], [day1, day2]))
print('ymd = ')
print(ymd)

# convert ymd to day of year
doy = ymd2doy(ymd)
print('\ndoy = ')
print(doy)

# convert day of year to ymd
(yr, mo, day) = doy2ymd(yr, doy)
print('\nymd =')
print(yr, mo, day)
