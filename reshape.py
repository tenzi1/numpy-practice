import numpy as np

#arange(start, end)
a = np.arange(1, 7)  #[1 2 3 4 5 6]
a = np.arange(2, 4)  #[2 3]
a = np.arange(50, 56) #[50 51 52 53 54,55]

#reshape
b = a.reshape((2,3))
# print(b)
# print(b.shape)
# print(b.size)


#np.newaxis
# a = np.arange(1,7)
# b = a[:, np.newaxis]
# c = a[np.newaxis, :]
# print(b)
# print(c)

# a = np.arange(1,5)
# b = np.arange(5,10)
# c = np.concatenate((a,b))
# print(c)

# a = np.arange(1,9)
# b = np.arange(9,17)
# print('a', a)
# print('b', b)
# a1 = a.reshape((2,4))
# b1  = b.reshape((2,4))
# print(a1)
# print(b1)
# c = np.concatenate((a1,b1))
# print(c)

#hstack
# a = np.arange(1,4)
# b = np.arange(3,6)
# c = np.hstack((a,b))
# print(c)
# d = np.vstack((a,b))
# print(d)

# e = np.concatenate((a,b))
# print('e',e)
# f = np.concatenate((a,b), axis=None)
# print('f', f)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

c = np.concatenate((a,b.T), axis=1)
print('c',c)

print(b.T)

