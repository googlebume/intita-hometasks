class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drive(self):
        print("Авто їде")

car1 = Car("Toyota", 2010)
car2 = Car("BMW", 2018)
car3 = Car("Tesla", 2022)

car1.drive()
car2.drive()
car3.drive()
