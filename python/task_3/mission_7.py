class Student():
    grades = []

    def __init__(self, name, grades ):
        self.name = name
        self.grades = grades
    
    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"grade {grade} given to student {self.name}")

    def calc_avarage(self):
        a = m
        return sum(self.grades) / len(self.grades)
    
student_1 = Student("Serhii", [1, 2, 12, 6, 2])

print("Середнє 1 " + student_1.calc_avarage())
student_1.add_grade(12)
print("Середнє 2 " + student_1.calc_avarage())