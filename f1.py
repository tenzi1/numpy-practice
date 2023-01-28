import numpy as np

# print(np.__version__)


#create array
a = np.array([1,2,3])
print(a)

#shape checking of array
print(a.shape)

#data type of array
print(a.dtype)

#number of dimension
print(a.ndim)

#size of array= number of elements in array
print(a.size)

#size of array element in Bytes
print(a.itemsize)

#accessing item of array = use index based access
print(a[0])

#asigning value to array
a[0] = 10
print(a)

#array multiplication
b = a * np.array([1,2,3])
print(b)