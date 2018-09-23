# 모듈은 단지 파이썬 코드의 파일
# import 문을 사용하여 다른 모듈의 코드를 참조한다.
import report
import sys

# description = report.get_description()
#
# print("Today's weather", description)
#
# for place in sys.path:
#     print(place)

# 파이썬 표준 라이브러리에는 유용한 모듈들이 다수 포진 되어 있다.

# 1. 누락된 키 처리하기
# periodic_table = {'Hydrogen': 1, "Helium": 2}
# print(periodic_table)
# carbon = periodic_table.setdefault('Carbon', 12)
# print(carbon)
# print(periodic_table)
#
# from collections import defaultdict
#
# periodic_table = defaultdict(int)
# print(periodic_table['Hydrogen'])


# dict_counter = {}
# for food in ['spam', 'spam', 'eggs', 'spam']:
#     if not food in dict_counter:
#         dict_counter[food] = 0
#     dict_counter[food] += 1
#
# for food, count in dict_counter.items():
#     print(food, count)

# 항목 세기
from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)
print(breakfast_counter & lunch_counter)
