from functools import reduce
l = [1,2,34,457,53,655,65, 55, 45]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))