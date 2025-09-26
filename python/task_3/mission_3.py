class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 8)

print(f"Прямокутник 1: площа = {rect1.area()}, периметр = {rect1.perimeter()}")
print(f"Прямокутник 2: площа = {rect2.area()}, периметр = {rect2.perimeter()}")
print(f"Прямокутник 3: площа = {rect3.area()}, периметр = {rect3.perimeter()}")
