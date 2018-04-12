print("hello world")

# 문자열 포매팅

age = 20
name = 'Swaroop'

print('{0} was  {1} years old when he wrote this book'.format(name, age))
print('why is {0} playing with that python?'.format(name))
print('This is the first line\nThis is the second line')

a1 = 3
a2 = 5
b1 = 'a'
b2 = 'b'
print(a1 + a2)
print(b1 + b2)
print("hello", a1)
'''
파이썬은 문자끼리의 더하기 및 곱하기를 할 수 있다. (java의 append)
'''

# 조건문 및 반복문

'''
number = 23
running = True
guess = int(input('Enter an Integer:'))

if guess == number:
    print("same")

elif guess < number:
    print("less")
else:
    print("bigger")

print('done')


while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print("same")
        running  = False
    elif guess<number:
        print("No, it is a little higher than that")
    else:
        print("No, it is a little lower than that.")
else:
    print('the while loop is over')

print('Done')
'''
'''
for i in range(1,5):
    print(i)

else:
    print('the for loop is over')
'''

'''

while True:
    s = input("Enter something : ")
    if s == 'quit':
        break
    if(len(s) <3):
        print('Too small')
        continue
    print('input is of sufficient length')
'''

# 함수
'''
def say_hello():
    print('hello world')

say_hello()
say_hello()

def print_max(a,b):
    if a>b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to",b)
    else:
        print(b,'is maximum')

print_max(3,4)
x=5
y=7
print_max(x,y)

x = 50
def func(x):
    print ('x is', x)
    x =2
    print("changed local x to",x)

func(x)
print('x is still',x)
'''
'''
x=50
def func2():
    global x

    print('x is',x)
    x=2
    print('changed global x to',x)
func2()
print('Value of x is',x)

def func3(message, times =1):
    print(message * times)
func3('Hello')
func3('World',5)
'''
'''
def func4(a,b=5,c=10): # 초기화를 파라미터에서 해줄 수 있음.
    print('a is',a,'and b is',b,'and c is',c)

func4(3,7)
func4(25, c=24)
func4(c=50, a =100)
'''
'''
# 파라미터 앞에 *, ** 의미
def func5(ini=5,*numbers,**keywords):
    count = ini
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(func5(10,1,2,3,vegetables=50,fruits=100))

def func6():
    pass
'''
def func7(x,y):
    '''Prints the maximum of two numbers.
     The two values must be integers. jay'''
    x = int(x)
    y = int(y)

    if x>y:
        print(x,'is maximum')
    else:
        print(y, 'is maximum')

func7(3,5)
print(func7.__doc__)