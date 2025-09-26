class Animal:
    def speak(self):
        print("Якась тварина видає звук")

class Dog(Animal):
    def speak(self):
        print("Гав!")

class Cat(Animal):
    def speak(self):
        print("Мяу!")


animals = [Animal(), Dog(), Cat(), ]

for a in animals:
    a.speak()
