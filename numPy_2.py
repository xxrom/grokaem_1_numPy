import numpy as np

a = np.zeros((1, 4))
b = np.zeros((4, 3))

c = a.dot(b)
print('shape:', a.shape, 'X', b.shape, '=', c.shape)

A = np.array([[1, 2, 3, 4]])  # ((1,4))
# B = np.array([[1, 2, 3, 4], [10, 20, 30, 40]]) # WRONG shape ! ((2,4))
B = np.array([[1, 10], [2, 20], [3, 30], [4, 40]])  # CoRRECt ! (4,2)
C = A.dot(B)
print(C)  # [[1*1 + 2*2 + 3*3 + 4*4], [1*10 + 2*20 + 3*30 + 4*40]] = [30, 300]
