class Dog:
    dog_num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.dog_num += 1
    
    def bark(self):
        print(f"Гавкнула собака {Dog.dog_num}")

dog_1 = Dog("Жорік ням-ням", 18).bark()
dog_2 = Dog("Жмурік", "1000-7").bark()