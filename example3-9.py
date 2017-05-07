'''
Example 3.9

Companion code for Fundamentals of Astrodynamics and Applications 2007
By David Vallado

Author:
Alex Willison
aawillison@gmail.com
'''

# required imports
from numpy import array
from timeconversions import hms2rad
from timeconversions import rad2hms

# first hms (from Vallado example)
hr1 = 15
mi1 = 15
sec1 = 53.63

# second hms (first hms +1 sec)
hr2 = 15
mi2 = 15
sec2 = 54.63

# arrange hms in column vectors
hms = array(([hr1, hr2], [mi1, mi2], [sec1, sec2]))
print('hms = ')
print(hms)

# convert hms to radians
rad = hms2rad(hms)
print('\nrad = ')
print(rad)

# convert radians to hms
hms = rad2hms(rad)
print('\nhms =')
print(hms)
