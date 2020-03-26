import numpy as np

a = np.array([0, 1, 2, 3])  # vector
b = np.array([4, 5, 6, 7])  # vector
c = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])  # matrix
d = np.zeros((2, 4))  #  (nRows X nColumns) 2x4 matrix of zeroes
e = np.random.rand(2, 5)  # 2x5 matrix of random in interval - [0,1]

print(a)
print(b)
print(c)
print(d)
print(e)

print(a * 0.1)  # vector * scalar
print(c * 0.2)  # vector * scalar
print(a * b)  # vector * vector
print(a * b * 0.2)  # vector * vector * scalar
print(a * c)  # vector * matrix => matrixNew(same size as matrix)
print(a * e)  # error => len(vector) != len(matrix[0])
