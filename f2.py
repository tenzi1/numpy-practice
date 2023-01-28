#LIST VS ARRAY
import numpy as np

lst = [1,2,3]
arr = np.array([1,2,3])

#we can append element to list with append() or adding +
#but same cannot be done to array

lst.append(4)
print(lst) #[1, 2, 3, 4]

# arr.append(4)
# print(arr)    #AttributeError: 'numpy.ndarray' object has no attribute 'append'


#Addition Operation ------------------------------------
lst = lst + [5]
print(lst) #Adds 5 to list

arr = arr + np.array([5])
print(arr) #[6 7 8] Adds 5 to all existing element of array

#MULTIPLICATION OPERATION with SCALER-----------------------------------------------
# LIST
lst = [1,2,3]
lst = lst * 2
print(lst) #[1, 2, 3, 1, 2, 3] -- elements are repeated twice

#ARRAY
arr = np.array([1,2,3])
arr = arr * 2
# print(arr) #[2 4 6] -- multiplies every element of array by scaler

