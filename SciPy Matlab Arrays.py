
"""Working With Matlab Arrays
We know that NumPy provides us with methods to persist the data in readable formats for Python. But SciPy provides us with interoperability with Matlab as well.

SciPy provides us with the module scipy.io, which has functions for working with Matlab arrays."""



"""Exporting Data in Matlab Format
The savemat() function allows us to export data in Matlab format.

The method takes the following parameters:

filename - the file name for saving data.
mdict - a dictionary containing the data.
do_compression - a boolean value that specifies whether to compress the result or not. Default False."""


from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
io.savemat('arr.mat', {"vec": arr})

# Import:
#mydata = io.loadmat('arr.mat')
mydata = io.loadmat('arr.mat', squeeze_me=True)

#print(mydata)
print(mydata['vec'])