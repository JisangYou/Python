class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


hunter = Person('Elmer Fudd', 28)
print(hunter.name)
print(hunter.age)


# name -> self.name


class Car():
    def exclaim(self):
        print("I'm a Car!")


# inheritance
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")

    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()
print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())


class Person():
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


car = Car()
print(car.exclaim())
print(Car.exclaim(car))


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("inside the getter")
        return self.hidden_name

    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name

    name = property(get_name, set_name)


fowl = Duck('Howard')
print(fowl.name)
print(fowl.set_name('Daffy'))


class Duck2():
    def __init__(self, input_name):
        self.hidden_name = input_name

        @property
        def name(self):
            print('inside the getter')
            return self.hidden_name

        @name.setter
        def name(self, input_name):
            print('inside the setter')
            self.hidden_name = input_name


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)
