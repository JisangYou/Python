import numpy as np
import pandas as pd

# 출처 : https://doorbw.tistory.com/172

data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
        "year": [2014, 2015, 2016, 2015, 2016],
        "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                  index=["one", "two", "three", "four", "five"])
print(" == df == ")
print(df)

print(" == df['year'] == ")
print(df['year'])

print("df[['year','points']]")
print(df[['year', 'points']])

df['penalty'] = 0.5

print("df['penalty'] = 0.5")
print(df)

df['penalty'] = [0.1, 0.2, 0.3, 0.4, 0.5]  # python의 List나 numpy의 array
print(df)

# 새로운 열을 추가하기
df['zeros'] = np.arange(5)
print(df)

# Series를 추가할 수도 있다.
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
df['debt'] = val
print(df)
