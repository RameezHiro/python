class Employee:
    language = "Py"   # This is a class attribute
    salary = 1200000

rameez = Employee()
rameez.name = "Rameez"  # This is an object (instance) attribute
print(rameez.name, rameez.language, rameez.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.language, rohan.salary)

# Here name is object (instance) attribute and salary and language are class attributes
# as they directly belong to the class

