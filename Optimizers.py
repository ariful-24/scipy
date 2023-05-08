

"""Optimizers in SciPy
Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.

Optimizing Functions
Essentially, all of the algorithms in Machine Learning are nothing more than a complex equation that needs to be minimized with the help of given data."""

#Find root of the equation x + cos(x):

# from scipy.optimize import  root
# from math import cos
#
# def eqn(x):
#     return x+ cos(x)
#
# myroot = root(eqn,0)
# print(myroot.x)
# print(myroot)

"""Minimizing a Function
A function, in this context, represents a curve, curves have high points and low points.

High points are called maxima.

Low points are called minima.

The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.

The lowest point in whole curve is called global minima, whereas the rest of them are called local minima."""

from scipy.optimize import minimize

def eqn(x):
    return x**2+x+2

mymin = minimize(eqn,0, method='BFGS')
print(mymin)

