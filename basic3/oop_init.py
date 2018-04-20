class Person:
    '''
    init 메소드는 클래스가 인스턴스화 될 때 호출
     따라서 이 메소드는 객체가 생성될 때 여러가지 초기화 명령들이 필요할 때 유용하게 사용
     여기서 init의 앞과 뒤에 있는 밑줄은 두번씩 입력해야 한다는 점 기억
    '''

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello, my name is", self.name)


p = Person('Swaroop')
p.say_hi()
