a = int(input("Enter your age: "))

# If statement no: 1
if(a%2  ==0):
    print("a is even")

# If statement no: 2
if(a>=18):
    print("you are above the age of consent")

elif(a<0):
    print("you are entering an invalid  negative age")

else:
    print("you are below the age of consent")

print('End of program')