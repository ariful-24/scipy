

"""Constants in SciPy
As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.

These constants can be helpful when you are working with Data Science."""

from scipy import constants

print(constants.pi)



"""Constant Units
A list of all units under the constants module can be seen using the dir() function."""

print(dir(constants))

"""Metric (SI) Prefixes:
Return the specified unit in meter (e.g. centi returns 0.01)"""

print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21


"""Binary Prefixes:
Return the specified unit in bytes (e.g. kibi returns 1024)"""

print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)    #1125899906842624


"""Mass:
Return the specified unit in kg (e.g. gram returns 0.001)"""

print(constants.gram)        #0.001
print(constants.metric_ton)  #1000.0
print(constants.grain)       #6.479891e-05
print(constants.lb)          #0.45359236999999997
print(constants.pound)       #0.45359236999999997


"""Angle:
Return the specified unit in radians (e.g. degree returns 0.017453292519943295)"""

print(constants.degree)     #0.017453292519943295
print(constants.arcmin)     #0.0002908882086657216
print(constants.arcminute)  #0.0002908882086657216

"""Time:
Return the specified unit in seconds (e.g. hour returns 3600.0)"""

print(constants.minute)      #60.0
print(constants.hour)        #3600.0
print(constants.day)         #86400.0

