# 1. Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)

print("Size:", arr.size)

print("Data Type:", arr.dtype)

print("Number of Dimensions:", arr.ndim)

# =========================================================================

# 2.	Create two NumPy arrays of 5 integers each. Perform and display:
# •	Addition 
# •	Subtraction 
# •	Multiplication 
# •	Division 
# •	Modulus

a = np.array([10,20,30,40,50])
b = np.array([2,4,5,8,10])
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)

# ===========================================================================

# 3. Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements.

a = np.array([12,25,8,45,32,19,50,7,28,15])
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))
print("Average:", np.mean(a))

# =============================================================================

# 4. Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.

a = np.arange(1,21)
print("Even numbers:", a[a%2==0])
print("Odd numbers:", a[a%2!=0])

# =============================================================================

# 5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
# •	2 × 6 matrix 
# •	3 × 4 matrix 
# •	4 × 3 matrix

a = np.arange(1,13)
print("2 x 6:")
print(a.reshape(2,6))
print("3 x 4:")
print(a.reshape(3,4))
print("4 x 3:")
print(a.reshape(4,3))

# ==============================================================================

# 6. Create two 3 × 3 NumPy matrices and perform matrix addition.

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(a+b)

# =============================================================================

# 7. Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8],[9,10],[11,12]])
print(np.dot(a,b))

# ==============================================================================

# 8. Create a 3 × 4 matrix and display its transpose.

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Original:")
print(a)
print("Transpose:")
print(a.T)
