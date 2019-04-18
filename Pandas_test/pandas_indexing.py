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

df['net_points'] = df['points'] - df['penalty']
df['high_points'] = df['net_points'] > 2.0
print(df)

print(" == df.columns == ")
print(df.columns)

df.index.name = 'Order'
df.columns.name = 'Info'

print(df)
# 0번째 부터 2(3-1) 번째까지 가져온다.
# 뒤에 써준 숫자번째의 행은 뺀다.
print(" == df[0:3]== ")
print(df[0:3])

# tow라는 행부터 four라는 행까지 가져온다.
# 뒤에 써준 이름의 행을 빼지 않는다.
print(" == df['two':'four'] == ")
print(df['two':'four'])  # 하지만 비추천!

# 아래 방법을 권장한다.
# .loc 또는 .iloc 함수를 사용하는 방법.
print(" == df.loc['two'] == ")  # 반환 형태는 Series
print(df.loc['two'])
print(" == df.loc['two':'four'] == ")
print(df.loc['two':'four'])
print(" == df.loc['two':'four', 'points'] == ")
print(df.loc['two':'four', 'points'])
print(" == df.loc[:,'year'] # == df['year'] ==")
print(df.loc[:, 'year'])
print(" == df.loc[:,['year','names']] == ")
print(df.loc[:, ['year', 'names']])
print("df.loc['three':'five','year':'penalty']")
print(df.loc['three':'five', 'year':'penalty'])
print(" == df.loc['six',:] = [2013,'Jun',4.0,0.1,2.1] == ")
df.loc['six', :] = [2019, "jisang", 1.7, 0.2, 1, -1.2, 1.5, False]
print(df)

# .iloc 사용:: index 번호를 사용한다.
print(" == df.iloc[3] == ")
print(df.iloc[3])

print(" == df.iloc[3:5, 0:2] == ")
print(df.iloc[3:5, 0:2])

print(df)
# year가 2014보다 큰 boolean data
print(" == df['year'] > 2014 == ")
print(df['year'] > 2014)

# year가 2014보다 큰 모든 행의 값
print(" == df.loc[df['year'] > 2014] == ")
print(df.loc[df['year'] > 2014])
# 상기와 비교
print(" == df.loc[df['year'] > 2014, :] == ")
print(df.loc[df['year'] > 2014, :])

print(df.loc[df['names'] == 'Kilho', ['names', 'points']])

# 새로운 값을 대입할 수도 있다.
print("df.loc[df['points'] > 3, 'penalty'] = 0")
df.loc[df['points'] > 3, 'penalty'] = 0
print(df)
