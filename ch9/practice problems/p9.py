with open("file.txt") as f:
    conten1 = f.read()


with open("poem.txt") as f:
    content2 = f.read()

if(conten1 == content2):
    print("Yes these files are identical")

else:
    print("No these files are not identical")
    
