# 유니버셜 함수
# ufunc라고 불리는 유니버셜 함수는 ndarray 안에 있는 데이터 원소별로 연산을 수행하는 함수다.
import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))

# 단항/ 이항 유니버셜 함수가 있다.

# 배열을 사용한 데이터 처리
# 넘피 배열을 사용해서 반복문을 명시적으로 제거하는 기법을 흔히 벡터화라고 한다. 이는 순수 파이썬 연산에 비해 빠르다.

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()

plt.title("graph")
plt.show()

# 배열 연산으로 조건절 표현하기
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# 하기의 표현식과
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)
# 하기의 표현식은 같다.
result2 = np.where(cond, xarr, yarr)
print(result2)
