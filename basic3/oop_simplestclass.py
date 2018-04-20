'''
파이썬의 self는 자바나 C,C++의 this와 같다.
ex)
MyClass라는 클래스를 생성했고, 이 클래스의 객체를 myobject 라는 이름으로 생성했다고 해 봅시다.
이제 이 객체의 메소드를 호출할 때는 myobject.method(arg1, arg2) 와 같이 하며, 이것은
파이썬에 의해 자동적으로 MyClass.method(myobject, arg1, arg2) 의 형태로 바뀌게 됩니
다. 이것이 self 에 대한 모든 것입니다.
'''

#  class
class Person:
    pass

p = Person()
print(p)

