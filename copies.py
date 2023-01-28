"""Copying numpy array"""
import numpy as np

a = np.array([1,2,3])
b = a
b[0] = 42
print(b) #[42  2  3]
print(a)    #[42  2  3]

#Here both a and b points same array in memory so if one is modiefied
#other is also affected

#solution
a = np.array([1,2,3])
b = a.copy()
b[0] = 42
print(b) #[42  2  3]
print(a) #[1 2 3]