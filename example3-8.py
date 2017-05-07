'''
Example 3.8

Companion code for Fundamentals of Astrodynamics and Applications 2007
By David Vallado

Author:
Alex Willison
aawillison@gmail.com
'''

# required imports
from numpy import array
from timeconversions import dms2rad
from timeconversions import rad2dms

# first dms (from Vallado example)
deg1 = -35
ami1 = -15
asec1 = -53.63

# second dms (first dms +1 asec)
deg2 = -35
ami2 = -15
asec2 = -54.63

# arrange dms in column vectors
dms = array(([deg1, deg2], [ami1, ami2], [asec1, asec2]))
print('dms = ')
print(dms)

# convert dms to radians
rad = dms2rad(dms)
print('\nrad = ')
print(rad)

# convert radians to dms
dms = rad2dms(rad)
print('\ndms =')
print(dms)
