'''
Time Conversion Functions

Companion code for Fundamentals of Astrodynamics and Applications 2007
By David Vallado

List of Functions:
dms2rad - degrees, arcminutes, arcseconds to radians
rad2dms - radians to degrees, arcminutes, arcseconds
hms2rad - hours, minutes, seconds to radians
rad2hms - radians to hours, minutes, seconds
hms2sec - hours, minutes, seconds to seconds
sec2hms - seconds to hours, minutes, seconds
mdarray - month day array
ymd2doy - year, month, day to day of year
doy2ymd - day of year to year, month, day
ymdhms2doy - year, month, day, hour, minute, second to day of year
doy2ymdhms - day of year to year, month, day, hour, minute, second
ymdhms2jd - year, month, day, hour, minute, second to Julian date
jd2ymdhms - Julian date to year, month, day, hour, minute, second

Author:
Alex Willison
aawillison@gmail.com
'''

# required imports
from numpy import array
from numpy import fix
from numpy import pi
from numpy import shape
from numpy import tile
from numpy import where
from numpy import zeros

def dms2rad(dms):
    """Convert degrees, arcminutes, and arcseconds to radians.  Based on the
    "DMSToRad" algorithm by David Vallado.

    inputs:
    dms = degree, arcminute, and arcsecond column vectors (0-359), (0-59),
        (0.0-59.999)

    outputs:
    rad = radians (0-6.282)
    
    call:
    rad = dms2rad(dms)
    """
    rad = (dms[0,:] + dms[1,:]/60.0 + dms[2,:]/3600.0)*pi/180.0
    return rad

def rad2dms(rad):
    """Convert radians to degrees, arcminutes, and arcseconds.  Based on the
    "RadToDMS" algorithm by David Vallado.

    inputs:
    rad = radians (0-6.282)

    outputs:
    dms = degree, arcminute, and arcsecond column vectors (0-359), (0-59),
        (0.0-59.999)
        
    call:
    dms = rad2dms(rad)
    """
    temp = rad*180.0/pi
    # initialize dms matrix
    dms = array(zeros((3,shape(rad)[0])))
    dms[0,:] = fix(temp)
    dms[1,:] = fix((temp - dms[0,:])*60.0)
    dms[2,:] = (temp - dms[0,:] - dms[1,:]/60.0)*3600.0
    return dms

def hms2rad(hms):
    """Convert hours, minutes, and seconds to radians.  Based on the
    "HMSToRad" algorithm by David Vallado.

    inputs:
    hms = hour, minute, and second column vectors (0-23), (0-59),
        (0.0-59.999)

    outputs:
    rad = radians (0-6.282)
    
    call:
    rad = hms2rad(hms)
    """
    temp = 15.0*pi/180.0
    rad = (hms[0,:] + hms[1,:]/60.0 + hms[2,:]/3600.0)*temp
    return rad

def rad2hms(rad):
    """Convert radians to hours, minutes, and seconds.  Based on the
    "RadToHMS" algorithm by David Vallado.

    inputs:
    rad = radians (0-6.282)

    outputs:
    hms = hour, minute, and second column vectors (0-23), (0-59),
        (0.0-59.999)
        
    call:
    hms = rad2hms(rad)
    """
    temp = rad/15.0*180.0/pi
    # initialize hms matrix
    hms = array(zeros((3,shape(rad)[0])))
    hms[0,:] = fix(temp)
    hms[1,:] = fix((temp - hms[0,:])*60.0)
    hms[2,:] = (temp - hms[0,:] - hms[1,:]/60.0)*3600.0
    return hms

def hms2sec(hms):
    """Convert hours, minutes, and seconds to seconds.  Based on the
    "HMSToTime" algorithm by David Vallado.

    inputs:
    hms = hour, minute, and second column vectors (0-23), (0-59),
        (0.0-59.999)

    outputs:
    sec = seconds (0.0-86400.0)
    
    call:
    sec = sec2hms(hms)
    """
    sec = hms[0,:]*3600.0 + hms[1,:]*60.0 + hms[2,:]
    return sec

def sec2hms(sec):
    """Convert seconds to hours, minutes, and seconds.  Based on the
    "TimeToHMS" algorithm by David Vallado.

    inputs:
    sec = seconds (0.0-86400.0)

    outputs:
    hms = hour, minute, and second column vectors (0-23), (0-59),
        (0.0-59.999)
    
    call:
    hms = sec2hms(sec)
    """
    temp = sec/3600.0
    # initialize hms matrix
    hms = array(zeros((3,shape(sec)[0])))
    hms[0,:] = fix(temp)
    hms[1,:] = fix((temp - hms[0,:])*60.0)
    hms[2,:] = (temp - hms[0,:] - hms[1,:]/60.0)*3600.0
    return hms

def mdarray(yr):
    """Create an array of months with number of days.  Based on part of
    the "YMD to Day of Year" algorithm by David Vallado.

    inputs:
    yr = year (1900-2100)

    outputs:
    md = month day array [31,(28,29),31,30,31,30,31,31,30,31,30,31]
    
    call:
    md = mdarray(yr)
    """
    print(yr)
    tempMd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(tempMd)
    md = tile(tempMd, [1,shape(yr)[0],1])
    print(md)
    temp = where(((yr - 1900)%4 == 0), 28, 29)
    print(temp)
    temp = [0,1]
    md[leapYr,1] = 29
    print(md)
    #if ((yr - 1900)%4 == 0):
    #    md[1] = 29
    return md

def ymd2doy(ymd):
    """Convert year, month, and day to equivalent day of year.  Based on
    the "YMD to Day of Year" algorithm by David Vallado.

    inputs:
    yr = year (1900-2100)
    mo = month (1-12)
    day = day (1-28,29,30,31)

    outputs:
    doy = day of year (0.0-366.0)
    
    call:
    doy = ymd2doy(yr, mo, day)
    """
    # create array of months with number of days
    md = mdarray(ymd[0,:])
    print(md)
    # calculate the day of year
    doy = sum(md[0:(mo-1)]) + day
    return doy

def doy2ymd(yr, doy):
    """Convert day of year to equivalent year, month, and day.  Based on
    the "Day of Year to YMD" algorithm by David Vallado.

    inputs:
    yr = year (1900-2100)
    doy = day of year (0.0-366.0)

    outputs:
    yr = year (1900-2100)
    mo = month (1-12)
    day = day (1-28,29,30,31)
    
    call:
    (yr, mo, day) = doy2ymd(yr, doy)
    """
    # create array of months with number of days
    md = mdarray(yr)
    # calculate the month and day
    tempDoy = int(doy)
    tempDy = 0
    tempMo = 0
    while (tempDoy > tempDy + md[tempMo]) & (tempMo < 11):
        tempDy = tempDy + md[tempMo]
        tempMo = tempMo + 1
    mo = tempMo + 1
    day = tempDoy - tempDy
    return (yr, mo, day)

def ymdhms2doy(yr, mo, day, hr, mi, sec):
    """Convert year, month, day, hour, minute, and second to equivalent
    day of year.  Based on the "YMDHMS to Day of Year" algorithm by
    David Vallado.

    inputs:
    yr = year (1900-2100)
    mo = month (1-12)
    day = day (1-28,29,30,31)
    hr = hour (0-23)
    mi = minute (0-59)
    sec = second (0.0-59.999)

    outputs:
    doy = day of year (0.0-366.0)
    
    call:
    doy = ymdhms2doy(yr, mo, day, hr, mi, sec)
    """
    doy = ymd2doy(yr, mo, day)
    doy = doy + (hr/24.0 + mi/1440.0 + sec/86400.0)
    return doy

def doy2ymdhms(yr, doy):
    """Convert day of year to equivalent year, month, day, hour, minute,
    and second.  Based on the "DaysToYMDHMS" algorithm by David Vallado.

    inputs:
    yr = year (1900-2100)
    doy = day of year (0.0-366.0)

    outputs:
    yr = year (1900-2100)
    mo = month (1-12)
    day = day (1-28,29,30,31)
    hr = hour (0-23)
    mi = minute (0-59)
    sec = second (0.0-59.999)

    call:
    (yr, mo, day, hr, mi, sec) = doy2mdhms(yr, doy)
    """
    # calculate the year, month, and day
    (yr, mo, day) = doy2ymd(yr, doy)    
    tempDoy = int(doy)
    # calculate the hour, minute, and second
    sec = (doy - tempDoy)*86400.0
    (hr, mi, sec) = sec2hms(sec)
    return (yr, mo, day, hr, mi, sec)

def ymdhms2jd(yr, mo, dy, hr, mi, sec):
    """Convert datetime to Julian date.  Based on the
    "JDToGregorianDate" algorithm by David Vallado.

    inputs:
    yr = year (1900-2100)
    mo = month (1-12)
    dy = day (1-28,29,30,31)
    hr = hour (0-23)
    mi = minute (0-59)
    sec = second (0.0-59.999)
    
    outputs:
    jd = Julian date (days from 4713 BCE)

    call:
    jd = ymdhms2jd(yr, mo, dy, hr, mi, sec)
    """
    jd = (367.0*yr
          - int((7*(yr + int((mo + 9)/12.0)))*0.25)
          + int(275*mo/9.0) + dy + 1721013.5
          + ((sec/60.0 + mi)/60.0 + hr)/24.0)
    return jd

def jd2ymdhms(jd):
    """Convert Julian date to datetime.  Based on the
    "GregorianDateToJD" algorithm by David Vallado.

    inputs:
    jd = Julian date (days from 4713 BCE)
    
    outputs:
    yr = year (1900-2100)
    mo = month (1-12)
    dy = day (1-28,29,30,31)
    hr = hour (0-23)
    mi = minute (0-59)
    sec = second (0.0-59.999)

    call:
    (yr, mo, dy, hr, mi, sec) = jd2ymdhms(jd)
    """
    temp = jd - 2415019.5
    tu = temp/365.25
    yr = 1900 + int(tu)
    leapYr = int((yr - 1901)*0.25)
    dy = temp - ((yr - 1900)*365.0 + leapYr)
    if dy < 1.0:
        yr = yr - 1
        leapYr = int((yr - 1901)*0.25)
        dy = temp - ((yr - 1900)*365.0 + leapYr)
    (yr, mo, day, hr, mi, sec) = doy2ymdhms(yr, dy)
    return (yr, mo, day, hr, mi, sec)
