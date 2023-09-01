import math
class Fraction:
    def __init__(self, num, den):
        self.n = num
        self.d = den

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    def __add__(self, other):
        numerator = self.n * other.d + other.n * self.d
        denominator = self.d * other.d
        return "{}/{}".format(numerator , denominator)
        
    def __sub__(self, other):
        numerator = self.n * other.d  -  other.n * self.d
        denominator = self.d * other.d
        return "{}/{}".format(numerator , denominator)
        
    def __mul__(self, other):
        numerator = self.n * other.n
        denominator = self.d * other.d
        return "{}/{}".format(numerator , denominator)
    
    def __truediv__(self, other):
        # 3/2 * 5/4 
        numerator   = self.n * other.d 
        denominator = self.d * other.n 
        return "{}/{}".format(numerator , denominator)
    
x = Fraction(3,4)
y = Fraction(5,6)

print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print(x / y)

