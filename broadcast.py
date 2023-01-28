import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = [1,0,1]
y = x + b
# print(y)

a = np.array([[7,8,9,10,11,12,13],[17,18,19,20,21,22,23]])
# print(a)
# print(a.sum())
# print(a.sum(axis=0)) # calculates sum of row element in same column
# print(a.sum(axis=1)) # calcultes sum of column elements in same row

print(a.mean()) #Overall mean 
print(a.mean(axis=0)) #Calculates mean of each column
print(a.mean(axis=1)) #Calculates mean of each row