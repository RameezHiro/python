class Number:
   def __init__(self, n):
      self.n = n

   def __add__(self, num):
      return Number(self.n + num.n)

n = Number(1)
m = Number(2)

print((n + m).n)

