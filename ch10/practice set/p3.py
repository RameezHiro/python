class Demo:
    a = 4

o = Demo()
print(o.a)  # Prints the class attribute bcuz instance attr is not present

o.a = 0 # Instance attr is set
print(o.a)# Prints the instance attribute bcuz instance attr is  present

print(Demo.a)  #Prints the class attr