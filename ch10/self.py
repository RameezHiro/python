class Employee:
    language = "Python"   # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning")

rameez = Employee()
# rameez.language = "Javascript"  # This is an object (instance) attribute
rameez.getInfo()
rameez.greet()
# Employee.getInfo(rameez)
