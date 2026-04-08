# class in oops
class Student:
    def info(self):
        print("This is a student class.")

# creating object
s1 = Student()
s1.info()

# constructor is used here 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Anurag", 23)

print(s1.name, s1.age)

# ATTRIBUTES & METHODS

class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def show(self):
        print("Company:", self.company)
        print("Model:", self.model)

car1 = Car("Tata", "Nexon")
car1.show()

# INHERITANCE 

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):   # child inherits parent
    def sound(self):
        print("Dog barks")

d = Dog()
d.speak()
d.sound()