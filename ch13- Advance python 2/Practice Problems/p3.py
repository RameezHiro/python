def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,34456,45767,53,65576,65, 55, 45]

f = list(filter(divisible5, a))
print(f)