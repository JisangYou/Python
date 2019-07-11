import numpy as np
from numpy.linalg import inv, qr

arr = np.arange(10)
np.save('some_array', arr)

print(np.load('some_array.npy'))

np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print(arch['b'])

# 선형 대수
X = np.random.randn(5, 5)
mat = X.T.dot(X)

print("inv(mat)", inv(mat))
print("mat.dot(inv(mat))", mat.dot(inv(mat)))

q, r = qr(mat)
print(r)

# 난수 생성
samples = np.random.normal(size=(4, 4))
print(samples)
