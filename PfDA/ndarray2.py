from array import array
import numpy as np

# 슬라이싱
d = np.arange(20).reshape(4, 5)
print(d[0:3, 1:3])

# 팬시색인

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr[[4, 3, 0, 6]])

arr2 = np.arange(15).reshape((3, 5))
print("arr2\n", arr2)

arr3 = np.arange(16).reshape((2, 2, 4))

print(arr3.transpose((1, 0, 2)))
# 축 바꾸기
print(arr3.swapaxes(1, 2))
