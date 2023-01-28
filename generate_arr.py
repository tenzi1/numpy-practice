"""Generating array methods"""
import numpy as np
a = np.zeros((2,3))
print(a)

b = np.zeros((4,5))
print(b)

c = np.ones((2,3))
print(c)

d = np.full((2,3), 5.0)
print(d)

e = np.full((3,3), 3, dtype=int)
print(e)

f = np.full((3,3), 'a')
print(f)

#Identity matrix
i = np.eye(3)
print(i)

#Equal step number generation using np.linspace
a = np.linspace(0, 10, 5)
print(a)