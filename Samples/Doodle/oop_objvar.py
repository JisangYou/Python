class Robot:
    population = 0

    def __init__(self, name):

        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):

        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):

        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):

        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()

'''
모든 것은 객체다
숫자, 문자열, 튜플, 리스트, 딕셔너리, 함수 = 객체
특히, 함수는 일등 시민으로써, 함수를 변수에 할당할 수 있고, 다름함수에서 이를 인자로 쓸 수 있음.
'''