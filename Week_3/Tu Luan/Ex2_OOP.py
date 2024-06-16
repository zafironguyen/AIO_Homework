class Ward():
    def __init__(self, name: str):
        self.name = name
        self.list_person = []

    def add_person(self, person):
        self.list_person.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.list_person:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.list_person:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.list_person = sorted(
            self.list_person, key=lambda x: x.yob, reverse=True)
        return self.list_person

    def compute_average(self):
        total = 0
        count = 0
        for person in self.list_person:
            if isinstance(person, Teacher):
                total += person.yob
                count += 1
        return total/count


class Student():
    def __init__(self, name: str, yob: int, grade: str) -> None:
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher():
    def __init__(self, name: str, yob: int, subject: str) -> None:
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor():
    def __init__(self, name: str, yob: int, specialist: str) -> None:
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


# 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
doctor1 = Doctor(name=" octorA", yob=1945, specialist="Endocrinologists")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

# 2(b)
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
# ward1.describe()

# 2(c)
print(f"\nNumber of doctors :{ward1.count_doctor()}")

# 2(d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
