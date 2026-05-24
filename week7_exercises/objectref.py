class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

s1 = Student("Kasun", 22, "A")
sptr = s1
sptr.age = 23

# Output answers:
print(s1.age)                # Output: 23
print(id(s1) == id(sptr))    # Output: True

# Bonus
students = [
    Student("Nimal", 25, "B"),
    Student("Amali", 23, "A"),
    Student("Kamal", 26, "C"),
]
