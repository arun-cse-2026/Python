# class & objects
class laptop:
    price =""
    processor =""
    ram =""

hp = laptop()
dell = laptop()

hp.price = "50000"
hp.processor = "i5"
hp.ram = "8gb"

dell.price = "60000"
dell.processor = "i7"
dell.ram = "16gb"

print(hp.price)
print(dell.price)



#attributes
class Student:
    def __init__(self, name, age):
        self.name = name    # attribute
        self.age = age     # attribute

s1 = Student("Alex", 20)
print(s1.name)
print(s1.age)

#methods
class Student:
    def greet(self):        # method
        print("Hello, I am a student")
s1 = Student()
s1.greet()

#encapsulation

class BankAccount:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount()
acc.deposit(5000)
acc.show_balance()

#inhertiance

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):   # Inheritance
    def bark(self):
        print("Dog barks")
class peacock(Dog):
    def sound(self):
        print("sound")
d = Dog()
d.speak()
d.bark()
d = peacock()
d.sound()


# polymorphsim (same method,diffrent actions)

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Bird()
p = Penguin()

b.fly()
p.fly()


#ABSTRACTION

from abc import ABC, abstractmethod
@abstractmethod
class Vehicle(ABC):
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

c = Car()
c.start()



