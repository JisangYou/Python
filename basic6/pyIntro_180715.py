# set
print(set('letters'))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

# set 심화
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# for, if 문

# for name, contents in drinks.items():
#     if 'vodka' in contents: print(name)

# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents): print(name)

# for name, contents in drinks.items():
#     if contents & {'vermouth', 'orange juice'}: print(name)

a = {1, 2}
b = {2, 3}
print("a.intersection(b)", a.intersection(b))
print("a | b ", a | b)
print("a.union(b) ", a.union(b))
print("a-b ", a - b)
print("a.difference(b) ", a.difference(b))
print("a^b", a ^ b)
print("a.symmetric_difference(b)", a.symmetric_difference(b))
print("a <= b", a <= b)
# 부분집합 여부
print("a.issubset(b)", a.issubset(b))

bruss = drinks['black russian']
wruss = drinks['white russian']

print("bruss & wruss", bruss & wruss)
print("bruss | wruss", bruss | wruss)
print("bruss - wruss", bruss - wruss)
print("wruss - bruss", wruss - bruss)
print("bruss ^ wruss", bruss ^ wruss)

# if 조건문

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

# while

# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#
# while True:
#     stuff = input("String to capitalize [type q to quit] : ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())
#
# while True:
#     value = input("Integer, please [q to quit]:")
#     if value == 'q':
#         break
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number, "squared is", number * number)

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    print('No even number found')

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
# key 값이 산출됨
for card in accusation: print(card)
# value 값이 산춤됨
for card in accusation.values(): print(card)
# key, value 모두 산출됨.
for card in accusation.items(): print(card)
