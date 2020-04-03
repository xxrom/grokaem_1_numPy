import numpy as np

a = np.zeros((1, 4))
b = np.zeros((4, 3))

c = a.dot(b)
print('0 shape:', a.shape, 'X', b.shape, '=', c.shape)

A = np.array([[1, 2, 3, 4]])  # ((1,4))
# B = np.array([[1, 2, 3, 4], [10, 20, 30, 40]]) # WRONG shape ! ((2,4))
B = np.array([[1, 10], [2, 20], [3, 30], [4, 40]])  # CoRRECt ! (4,2)
C = A.dot(B)
# [[1*1 + 2*2 + 3*3 + 4*4], [1*10 + 2*20 + 3*30 + 4*40]] = [30, 300]
print('1 shape: %s X %s = %s |' % (str(A.shape), str(B.shape), str(C.shape)), C)

a = np.zeros((2, 4))
b = np.zeros((4, 3))

c = a.dot(b)
print('2 shape: %s X %s = %s' % (str(a.shape), str(b.shape), str(c.shape)))

e = np.zeros((2, 1))
f = np.zeros((1, 3))
g = e.dot(f)
print('3 shape: %s X %s = %s' % (str(e.shape), str(f.shape), str(g.shape)))

h = np.zeros((5, 4)).T  # change rows with columns
i = np.zeros((5, 6))
j = h.dot(i)
print('4 shape: %s X %s = %s' % (str(h.shape), str(i.shape), str(j.shape)))

h = np.zeros((5, 4))
i = np.zeros((5, 6))
print('5 shape with error: %s X %s = error' % (str(h.shape), str(i.shape)))
j = h.dot(i)
print(str(j.shape))
