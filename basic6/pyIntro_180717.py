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
