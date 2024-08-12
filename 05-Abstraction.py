"""
 ? ABSTRACT CLASS
 1- Concept Abstract class
 2- Concept Abstract Method
 3- Example
"""

# abc => a:Abstract, b:Base, c: Class
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def macke_sound(self):
        pass


class Dog(Animal):
    def macke_sound(self):
        return "HawHaw"


class Cat(Animal):
    def macke_sound(self):
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.macke_sound())  # HawHaw
print(cat.macke_sound())  # Meow


# ====================================================


# TODO: Abstract Class
class Transport(ABC):
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

        @abstractmethod
        def move(self):
            pass

        @abstractmethod
        def stop(self):
            pass


class Car(Transport):
    def __init__(self, name):
        super().__init__(name, 4)

    def move(self):
        return f"{self.name} is moving on {self.wheels} wheels."

    def stop(self):
        return f"{self.name} has stopde."


class Plain(Transport):
    def __init__(self, name):
        super().__init__(name, 2)

    def move(self):
        return f"{self.name} is moving on {self.wheels} rafact."

    def stop(self):
        return f"{self.name} has stopde."


# Using Classe
car = Car("Toyota ")
plain = Plain("356 ")
print(car.move())
print(car.stop())


print(plain.move())
print(plain.stop())
