class Employee:
    language = "Python"   # This is a class attribute
    salary = 1200000

rameez = Employee()
rameez.language = "Javascript"  # This is an object (instance) attribute
print(rameez.language, rameez.salary)
