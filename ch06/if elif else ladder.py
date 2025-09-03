a = int(input("Enter your age: "))

# If elif else ladder

if(a>=18):
    print("you are above the age of consent")

elif(a<0):
    print("you are entering an invalid  negative age")

elif(a==0):
    print("you are entering 0")

else:
    print("you are below the age of consent")

print('End of program')