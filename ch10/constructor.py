class Employee:
    language = "Python"   # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):  # dunder method which is automatically called
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language
        
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning")

rameez = Employee("Rameez", 1300000, "JavaScript")
# rameez.name = "Rameez"
print(rameez.name, rameez.salar, rameez.language)

# rohan = Employee()