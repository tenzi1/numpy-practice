"""Random number generations"""
import numpy as np

a = np.random.random((3,2))
print(a)

a = np.random.randn(1000)
print(a.mean(), a.var())


a = np.random.randint(3,10,size=(3,3))
print(a)

b = np.random.randint(1,10, size=(4,4))
print(b)