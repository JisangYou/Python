# 모듈은 단지 파이썬 코드의 파일
# import 문을 사용하여 다른 모듈의 코드를 참조한다.
import report
import sys

description = report.get_description()

print("Today's weather", description)

for place in sys.path:
    print(place)
