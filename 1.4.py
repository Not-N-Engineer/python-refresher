import numpy as np

# Problem 1
print("_____Problem 1_____")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)

# Problem 2
print("_____Problem 2_____")
a = np.array([[1, 2], 
              [3, 4]])
b = np.array([[5, 6], 
              [7, 8]])
print(a + b)
print(a - b)

# Problem 3
print("_____Problem 3_____")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a.dot(b))

# Problem 4
print("_____Problem 4_____")
a = np.array([[1, 2, 3], 
              [4, 5, 6]])
b = np.array([[ 7,  8,  9, 10], 
              [11, 12, 13, 14], 
              [15, 16, 17, 18]])
print(a.dot(b))

# Problem 5
print("_____Problem 5_____")
a = np.array([1, 1, 2])
print(np.linalg.norm(a))

# Problem 6
print("_____Problem 6_____")
a = np.array([[1, 2], 
              [3, 4]])
print(a.T)