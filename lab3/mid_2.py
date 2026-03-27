class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def get_info(self):
        avg = sum(self.grades) / len(self.grades) if self.grades else 0
        return (f"Студент: {self.name}, Группа: {self.group}, "
                f"Средний балл: {avg:.2f}")


student = Student("Иванов Иван", "ПИ-201", [5, 4, 5, 3, 4])
print(student.get_info())
