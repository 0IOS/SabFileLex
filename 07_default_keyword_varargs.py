# Default Arguments
def greet(name, message="Good Morning"):
    print("Hello", name + ",", message)

print("--- Default Arguments ---")
greet("Alice")
greet("Bob", "Good Evening")

print()

# Keyword Arguments
def student_info(name, roll, branch):
    print("Name:", name)
    print("Roll:", roll)
    print("Branch:", branch)

print("--- Keyword Arguments ---")
student_info(name="Rahul", roll=101, branch="CS")
student_info(branch="IT", name="Priya", roll=102)

print()

# Variable Length Arguments
def total_marks(*marks):
    total = sum(marks)
    print("Marks obtained:", marks)
    print("Total marks:", total)

print("--- Variable Length Arguments ---")
total_marks(80, 75, 90, 85, 70)
total_marks(60, 55, 70)
