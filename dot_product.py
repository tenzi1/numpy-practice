#DOT PRODUCT = SUM of product of corresponding items of array

#implementation  using list
import numpy as np
from timeit import default_timer as timer
l1 = [1,2,3]
l2 = [4,5,6]

def dot_product(l1, l2):
    dot = 0
    for i in range(len(l1)):
        dot += l1[i] * l2[i]
    print(dot)

dot_product(l1, l2)


# implementation using ARRAY
arr1 = np.array(l1)
arr2 = np.array(l2)

dot = np.dot(arr1, arr2)

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T = 1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
    return dot

def dot2():
    return np.dot(a,b)


start = timer()
for t in range(T):
    dot1()
stop = timer()
t1 = stop - start

start= timer()
for t in range(T):
    dot2()
stop = timer()
t2 = stop - start

print("list calculation", t1) #list calculation 0.8259787000715733
print("np.dot", t2)           #np.dot 0.015368400141596794
print('ratio', t1/t2)         #ratio 53.74526251668465


# Hence numpy array is lot faster than python list






