# for, break 문
cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print('this shop has some lovely', cheese)
    break

if not found_one:
    print('this is not much of a cheese shop, is it?')

# zip 문

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# zip 활용법
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list(zip(english, french)))
print(dict(zip(english, french)))

# range
# 컴퓨터의 메모리를 전부 사용하지 않고, 프로그램의 충돌없이 아주 큰 범위를 생성할 수 있게 해준다.
# range(start, stop, step)

for x in range(0, 3):
    print(x)
print(list(range(0, 3)))
print(list(range(0, 11, 2)))

# comprehension 파이써닉한 방법

number_list = [number for number in range(1, 6)]
number_list2 = [number - 1 for number in range(1, 6)]
print("number_list", number_list)
print("number_list2", number_list2)

a_list = [number for number in range(1, 6) if number % 2 == 1]
print("a_list", a_list)

# 상기와 같은 의미.
# a_list = []
# for number in range(1,6):
#     if number % 2 ==1 :
#         a_list.append(number)
#
# print(a_list)

# 이중 반복문

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells: print(cell)

for row, col in cells:
    print(row, col)

# 굉장히 유용한 컴프리 헨션....
# 코드를 줄일 수 있고, 직관적으로 알고리즘을 생각할 수 있음.
