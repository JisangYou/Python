def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')


def buggy2(arg):
    result = []
    result.append(arg)
    print(result)


buggy2('a')
buggy2('b')


def buggy3(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


buggy3('a')
buggy3('b')


# 위치 인자 모으기 - *
def print_args(*args):
    print('Position argument tuple:', args)


print_args(3, 2, 1, 'wait', 'uh....')


# 키워드 인자 모으기 - **

def print_kwargs(**kwargs):
    print('Keyword arguments :', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaron')


# docstring - 함수 정의에 문서를 붙일 수 있다.

def echo(anything):
    'echo returns its input argument'
    return anything


help(echo)


# 일등 시민 : 함수, 모든 것이 객체다. 그러므로 함수를 변수에 할당할 수 있고, 다른 함수에서 이를 인자로 쓸 수 있으며, 함수에서 이를 반환 할 수 있다.

def answer():
    print(42)


answer()


def run_something(func):
    func()


# answer()이 아니라 answer를 전달했다. 함수를 인자로 취급할 수 있다.
run_something(answer)

print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


# 파이써닉한 구문
run_something_with_args(add_args, 5, 9)


# 파이써닉한 구문 2

def sum_args2(*args):
    return sum(args)


def run_with_positional_arg(func, *args):
    # 함수로 들어온 인자와 그 이후의 넣어준 인자를 인자로 들어온 함수에 넣어서 계산한다.
    return func(*args)


print(run_with_positional_arg(sum_args2, 1, 2, 3, 4))


# 내부 함수

def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)


print(outer(4, 7))


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote

    return inner(saying)


print(knights('Ni!'))


# 클로져-> 클로져는 다른 함수에 의해 동적을 생성된다. 그리고 바깥 함수로부터 생성된 변수값을 변경하고, 저장할 수 있는 함수다.

def knights2(saying):
    def inner2():
        return "We are the Knights who say: '%s'" % saying

    return inner2


a = knights('Duck')
b = knights('Hasenpfeffer')

print(a)
print(b)


# 익명함수
def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
    return word.capitalize() + '!'


edit_story(stairs, enliven)

'''
익명 함수 람다를 사용했을 시....
'''
edit_story(stairs, lambda word: word.capitalize() + '!')
