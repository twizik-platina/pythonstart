from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int

def info(student):
    print(f"{student.name}, {student.age} лет, {student.grade} класс")

def up_grade(student):
    student.grade += 1

def check_sovershenolet(student):
    return student.age >= 18

def vozrast_students(s1, s2):
    if s1.age > s2.age:
        return f"{s1.name} старше"
    elif s1.age < s2.age:
        return f"{s2.name} старше"
    return "Одного возраста"

ivan = Student("Иван", 14, 8)
maria = Student("Мария", 14, 7)

info(ivan)
info(maria)
up_grade(ivan)
print(f"Новый класс Ивана: {ivan.grade}")
print(f"Иван совершеннолетний: {check_sovershenolet(ivan)}")
print(f"Мария совершеннолетний: {check_sovershenolet(maria)}")
print(vozrast_students(ivan, maria))