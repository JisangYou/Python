'''
제너레이터는 파이썬의 시퀀스를 생성하는 객체다.
일반 적인 함수는 이전 호출에 대한 메모리가 없고, 항상 똑같은 상태로 첫번 쨰 라인부터 수행한다.
'''
print(sum(range(1, 101)))


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(my_range)  # 이건 함수 취급
print(my_range(1, 5))  # 이건 제너레이터 취급

'''
데커레이터는 하나의 함수를 취해서 또 다른 함수를 반환하는 함수다.
 
'''


def document_it(func):
    def new_function(*args, **kwargs):
        '''

        :param args: 파라미터를 몇개 받을 지 모를때 사용하고, 튜플 형태로 전달됨.
        :param kwargs: 파라미터 명을 같이 전달할 수 있고, 딕셔너리 형태로 전달됨.
        :return:
        '''
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword argument', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


def add_ints(a, b):
    return a + b


# 수동 세팅
print(add_ints(3, 5))
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)


# 자동 세팅 및 중복 세팅 가능
@document_it
@square_it
def add_ints(a, b):
    return a + b


print(add_ints(4, 6))

'''
파이썬은 다양한 네임스페이스가 있다. 
네임 스페이스는 특정이름이 유일하고, 다른 네임스페이스에서의 같은 이름과 관계가 없는 것을 말한다. 
'''

animal = 'fruitbat'


def print_global():
    print('inside print_global:', animal)


print('at the top level:', animal)
print(print_global())


# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print("after the change:", animal)


def change_local():
    animal = 'wombat'
    print('locals:', locals())


'''
locals() 함수는 로컬 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
globals() 함수는 글로벌 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
'''

print(change_local())
print('globals:', globals())

'''
_와 __는 주로 예약어
'''


def amazing():
    '''
    This is the amazing function. want to see it again?
    '''
    print('This function is named:', amazing.__name__)
    print('And its docString is:', amazing.__doc__)


amazing()

'''
예외처리
'''
short_list = [1, 2, 3]
position = 5

try:
    short_list[position]
except:
    print('Need a postion between 0 and', len(short_list) - 1, 'but got', position)

# 여러 예외가 발생할 가능성이 있다면, 각 예외마다 특정 핸들러를 따로 사용하는 것이 좋다.

short_list2 = [1, 2, 3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list2[position])
    except IndexError as error:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

# 예외 만들기는 필요할 때!

