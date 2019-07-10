# 딕셔너리 컴프리헨션
word = 'letters'
# letter_counts = {letter: word.count(letter) for letter in word}
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# 셋 컴프리헨션
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

# 제너레이트 컴프리헨션
number_thing = (number for number in range(1, 6))
# for number in number_thing:
#     print(number)
number_list = list(number_thing)
print(number_list)


# 함수
def make_a_sound():
    print('quack')


make_a_sound()


def agree():
    return True


if agree():
    print('splendid!')
else:
    print('That was unexpected.')


# 위치인자
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu("chardonnay", 'chicken', 'cake'))

# 키워드 인자

print(menu(entree='beef', dessert='bagel', wine='bordeaux'))


def menu2(wine, entree, dessert="pizza"):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu2('chardonnay', 'chicken'))
