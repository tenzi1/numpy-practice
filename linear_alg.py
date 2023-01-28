import numpy as np

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors)
print(eigenvectors[:,0])

#e_vec * e_val = A * e_vec
b = eigenvectors[:,0] * eigenvalues[0]
print('e,',b)

c = a @ eigenvectors[:,0]
print('e', b)

#compare 
print(np.allclose(b,c))


#Solution of linear equeation Ax = B
# Process 1
A = np.array([[1,1],[1.5,4.0]])
B = np.array([2200,5050])
e_val, e_vec = np.linalg.eig(A)
print(e_vec)
print(e_val)

A_inv = np.linalg.inv(A)
x = A_inv.dot(B)

print(x)

# Recomended Process
x = np.linalg.solve(A, B)
print(x)
