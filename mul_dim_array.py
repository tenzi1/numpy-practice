import numpy as np

a = np.array([[1,2], [3,4]])
print(a)
print(a.shape)#(2, 2) first= number of rows, number of cols

b = np.array([[1,2,2], [4,5,6]])
print(b)
print(b.shape)


#array slicing
print(a[0:,0]) # a[row-index, col-index]

print(a[1, 1])

#array Transpose
print(a.T)

#Array Inverse
print(np.linalg.inv(a))

#Array Determinant
print(np.linalg.det(a))

#Array diagonal matrix
print(np.diag(a))

c = np.diag(a)
print(np.diag(c))


a = np.array([[1,2],[3,4]])
b = a[0,1]
print(b)

# a = np.array([[1,2],[3,4],[5,6]])
# print(a)
# print(a.ndim)
# print(a[-1,-1])
# print(a[1,1])


#Boolean mapping
# a = np.array([[1,2],[3,4],[5,6]])
# bool_idx = a > 2
# print(bool_idx)
# print(type(bool_idx))

# is_odd = a % 2 != 0
# print(is_odd)

# a = np.array([[1,2],[3,4],[5,6]])
# bool_idx = a > 2
# print(a[bool_idx])


# a = np.array([[1,2],[3,4],[5,6]])
# print(a[a>2])
# print(a)

#WHERE 
# a = np.array([[1,2],[3,4],[5,6]])
# b = np.where(a>2,a, -1)
# print(b)

# c = np.where(a % 2, a, 0)
# print(c)

# d = np.where(a % 2 != 0, a, 9)
# print(d)


#Multi index selection
# a = np.array([12,23,4,45,56,67,78])
# b = [1,3,5]
# print(a[b])



#NP.ARGWHERE
a = np.array([12,34,45,67,87,8,7])
even = np.argwhere(a%2==0).flatten()
print(even)
print(a[even])

a = np.array([12,34,45,67,87,8,7])
print(a[a%2==0])
