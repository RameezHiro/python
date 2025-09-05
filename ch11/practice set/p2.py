class Aniamls:
    pass

class Pets(Aniamls):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")
    
d = Dog()

d.bark()
