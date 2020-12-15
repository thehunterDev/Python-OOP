class Pets:
    def show(self):
        print("\033[1m" + f'My name is {self.name} and I am {self.age} years old. I am {self.color} and my owner\'s name is {self.owner_name}. Also, I am a {self.specie}')
class Dog(Pets):
    def __init__(self, name, age, color, owner_name):
        self.name = name
        self.age = age
        self.owner_name = owner_name
        self.color = color
        self.specie = "Dog"
class Cat(Pets):
    def __init__(self, name, age, color, owner_name):
        self.name = name
        self.age = age
        self.owner_name = owner_name
        self.color = color
        self.specie = "Cat"
class Fish(Pets):
    def __init__(self, name, age, color, owner_name):
        self.name = name
        self.age = age
        self.owner_name = owner_name
        self.color = color
        self.specie = "Fish"

a = Dog("John", 4, "Black", "Tim")
a.show()
b = Cat("Tom", 5, "White", "Bruno")
b.show()
c = Fish("Lenny", 2, "Blue and Red", "Carla")
c.show()
