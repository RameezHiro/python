

def f_to_c(f):
   return 5*(f-32)/9

f = int(input("Enter the temperature in F: "))
c = f_to_c(f)
print(f"{round(f_to_c(f), 2)} C")