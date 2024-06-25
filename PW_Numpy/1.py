#Before all used matlab
# Numpy--->Numerical Python
# Numpy is designed to perform matrix and array based calculations
# Numpy is used to do array and matrix manipulation  
import numpy as np
l=[1,2,3,4,5]
a=np.array(l)
print(a)
print(type(a))
arr=np.asarray(l)
print(arr)
print(type(arr))
# U can use array or asarray to get the array
# Suppose u have list and u want to convert it to an array
print(np.array([[1,2,34,5],[3,4,5,6,],[7,7,2,3]]))
# To check the dimensions of the array
arr=np.array([[1,2,34,5],[3,4,5,6,],[7,7,2,3]])
print(arr.ndim)
# Gives 2 as the output indicating that its 3 rows and 3 columns 
# ndim tells the dimensions of the array 


