f = open(r"C:\Users\Rameez\OneDrive\Documents\GITDEMO2\python\ch9\practice problems\poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")
f.close()
