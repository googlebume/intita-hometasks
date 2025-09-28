class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attrs(self):
        print(f"Person {self.name} has age {self.age}")


class Employee(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def print_employment_conditions(self):
        print(f"Employee {self.name} works as {self.position} asd receives a salary of {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position, salary)

    def manage(self):
        print("Manager manages this team")


emp = Employee("Ivan", 25, "Developer", 2000)
emp.print_attrs()
emp.print_employment_conditions()

mgr = Manager("Oksana", 30, "Team Lead", 4000)
mgr.print_attrs()
mgr.print_employment_conditions()
mgr.manage()
