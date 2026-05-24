
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


s1 = Student("Kasun", 22, "A")


sptr = s1
sptr.age = 23


print("--- Step 4 Verification ---")
print(f"s1.age: {s1.age}")  # Yes, it changed to 23 because sptr references the same object
print(f"id(s1) == id(sptr): {id(s1) == id(sptr)}")  # True

print("\n--- Step 5: Bonus Iteration ---")
students = [
    Student("Nimal", 25, "B"),
    Student("Amali", 23, "A"),
    Student("Kamal", 26, "C")
]


for s in students:
    print(f"Name: {s.name}, Age: {s.age}, Grade: {s.grade}")


print("\n--- Step 6: Bonus 2 Comparison ---")
sptr2 = Student("Amali", 24, "B")

print(f"id(sptr2) == id(s1): {id(sptr2) == id(s1)}")  
