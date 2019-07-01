import numpy as np

# 2행 3열의 데이터
data = np.random.randn(2, 3)
print(data)

print(data.shape)
print(data.dtype)

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)

print(np.zeros((3, 6)))

print(np.arange(15))

# ndarray의 자료형
# 자료형 dtype은 ndarray가 특정 데이터를 메모리에서 해석하기 위해 필요한 정보를 담고 있는 특수한 객체이다.
# 대부분의 데이터는 디스크에서 데이터를 읽고 쓰기 편하도록 하위 레벨의 표현에 직접적으로 맞춰져 있으며, C나 포트란 같은 저수준 언어로 작성된 코드와 쉽게 연동이 가능하다.
arr3 = np.array([1, 2, 3], dtype=np.float64)
arr4 = np.array([1, 2, 3], dtype=np.int32)

print("arr1 == ", arr3)
print("arr2 == ", arr4)

arr5 = np.array([1, 2, 3, 4, 5])
print("arr5.dtype", arr5.dtype)

float_arr = arr5.astype(np.float64)
print("float_arr.dtype", float_arr.dtype)
