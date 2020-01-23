#3.3/3.4
from math import sqrt

class complex:
    """
    Class representation of complex numbers with operations.

    Attributes:
    a: Real part of complex number.
    b: Imaginary part of complex number.
    """

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        """
        Support friendly print() of complex class object.
        Returns string representation.
        """

        if self.b > 0:
            return "%g + %gi" % (self.a, self.b)

        else:
            return "%g - %gi" % (self.a, -self.b)

    def conjugate(self):
        """
        Returns the conjugate of a complex number.
        Return type is complex.
        """

        return complex(self.a, -self.b)

    def modulus(self):
        """
        Returns the modulus of a complex number.
        Return type is a float.
        """

        return sqrt(self.a**2 + self.b**2)

    def __add__(self, other):
        """
        Returns sum of complex number and float/int/other complex number.
        Return type is complex.
        """

        a, b = self.a, self.b
        if isinstance(other, complex):             #Addition for type complex and complex
            u, v = other.a, other.b
            return complex(a + u, b + v)

        else:
            real, imag = other.real, other.imag    #Addition for type complex and float/int/
            return complex(a + real, b + imag)     #pythons built in complex.

    def __sub__(self, other):
        """
        Returns difference of complex number and float/int/other complex number.
        Return type is complex.
        """

        a, b = self.a, self.b
        if isinstance(other, complex):             #Subtraction for type complex and complex
            u, v = other.a, other.b
            return complex(a, b) + complex(-u, -v) #Using __add__ method

        else:                                      #Subtraction for type complex and float, int,
            return complex(a, b) + -other          #or pythons built in complex

    def __mul__(self, other):
        """
        Returns product of complex number and float/int/other complex number.
        Return type is complex.
        """

        a, b = self.a, self.b
        if isinstance(other, complex):             #Multiplication for type complex and complex
            u, v = other.a, other.b
            return complex(a*u - b*v, a*v + b*u)

        else:                                      #Multiplication for type complex and float/int/complex
            real, imag = other.real, other.imag
            return complex(a*real - b*imag, a*imag + b*real)

    def __eq__(self, other):
        """
        Returns True if two complex numbers are equal. Else returns False
        """

        eps = 1e-16  #Allow small rounding errors
        if abs(self.a - other.a) <= eps and abs(self.b - other.b) <= eps:
            return True
        else:
            return False

    def __radd__(self, other):
        """
        Does b.__add__(a) if a.__add__(b) fails
        """

        return complex.__add__(self, other)

    def __rsub__(self, other):
        """
        Does -1*b.__sub__(a) if a.__sub__(b) fails
        """

        return -1*complex.__sub__(self, other)

    def __rmul__(self, other):
        """
        Does b.__mul__(a) if a.__mul__(b) fails
        """

        return complex.__mul__(self, other)

#DEMO
if __name__ == '__main__':
    myComplex1 = complex(1, 1)
    myComplex2 = complex(1, -1)

    #__str__
    print("__str__():")
    print("myComplex1: %s \nmyComplex2: %s\n" % (myComplex1, myComplex2))

    #__add__
    add = myComplex1 + myComplex2
    print("__add__():")
    print("myComplex1 + myComplex2: %s\n" % add)

    #__sub__
    sub = myComplex1 - myComplex2
    print("__sub__():")
    print("myComplex1 - myComplex2: %s\n" % sub)

    #__mul__
    mul = myComplex1*myComplex2
    print("__mul__():")
    print("myComplex1 * myComplex2: %s\n" % mul)

    #__add__, __sub__, __mul__ combination
    combo = 1 + 2*myComplex1*myComplex2 - myComplex1 + myComplex2
    print("combination:")
    print("1 + 2*myComplex1*myComplex2 - myComplex1 + myComplex2: %s\n" % combo)
