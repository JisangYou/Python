import numpy as np

# 수학과 통계메서드

arr = np.random.randn(5, 4)

print(arr)

print("arr.mean()", arr.mean())
print("np.mean(arr)", np.mean(arr))
print("arr.sum()", arr.sum())

bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 아래 두 함수는 같은 기능을 한다.
print(np.unique(names))
print(sorted(set(names)))
