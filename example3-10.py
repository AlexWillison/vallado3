'''
Example 3.10

Companion code for Fundamentals of Astrodynamics and Applications 2007
By David Vallado

Author:
Alex Willison
aawillison@gmail.com
'''

# required imports
from numpy import array
from timeconversions import hms2sec
from timeconversions import sec2hms

# first hms (from Vallado example)
hr1 = 13
mi1 = 22
sec1 = 45.98

# second hms (first time +1 sec)
hr2 = 13
mi2 = 22
sec2 = 46.98

# arrange hms in column vectors
hms = array(([hr1, hr2], [mi1, mi2], [sec1, sec2]))
print('hms = ')
print(hms)

# convert hms to seconds
sec = hms2sec(hms)
print('\nsec = ')
print(sec)

# convert seconds to hms
hms = sec2hms(sec)
print('\nhms =')
print(hms)
