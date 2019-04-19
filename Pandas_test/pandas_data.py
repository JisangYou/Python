import numpy as np
import pandas as pd

# 출처 : https://doorbw.tistory.com/172

# DataFrame을 만들때 index, column을 설정하지 않으면 기본값으로 0부터 시작하는 정수형 숫자로 입력된다.
df = pd.DataFrame(np.random.randn(6, 4))
print(" == pd.DataFrame(np.random.randn(6, 4)) == ")
print(df)

df.columns = ['A', 'B', 'C', 'D']
df.index = pd.date_range('20160701', periods=6)
# pandas에서 제공하는 date range함수는 datetime 자료형으로 구성된, 날짜 시각등을 알 수 있는 자료형을 만드는 함수
print(" == pd.date_range('20160701', periods=6) ==")
print(df.index)

print(" == df ==")
print(df)

# 행의 값중 하나라도 nan인 경우 그 행을 없앤다.
df.dropna(how='any')
print(" == df.dropna(how='any') ==")
print(df)

# 행의 값의 모든 값이 nan인 경우 그 행으 없앤다.
df.dropna(how='all')
print(" == df.dropna(how='all') == ")
print(df)

# nan값에 값 넣기
df.fillna(value=0.5)
print(" == df.fillna(value=0.5) == ")

# non값인지 확인하기
print(" == df.isnull() == ")
print(df.isnull())

print(pd.to_datetime('20160701'))

# 2개 이상도 가능
print(" == df.drop([pd.to_datetime('20160702'), pd.to_datetime('20160704')]) == ")
df.drop([pd.to_datetime('20160702'), pd.to_datetime('20160704')])
print(df)
