# 키 정렬하기 OrderedDict()
from collections import OrderedDict

quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Owl'),
    ('Curly', 'Nyuk nyuk!')
])

for stooge in quotes:
    print(stooge)


# 스택 + 큐 == 데크
# deque는 스택과 큐의 기능을 모두 가진 출입구가 양끝에 있는 큐다.
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


# 이해가 잘 안되는 범위?

print(palindrome('a'))
print(palindrome('as'))

# 코드 구조 순회하기: itertools

import itertools


# for item in itertools.cycle([1, 2]):
#     print(item)

# for item in itertools.accumulate([1, 2, 3, 4]):
#     print(item)

def multiply(a, b):
    return a * b


for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)

from pprint import pprint

quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk, nyuk!')
])

pprint(quotes)
