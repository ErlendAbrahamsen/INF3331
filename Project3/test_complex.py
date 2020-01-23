#3.2
from math import sqrt
from complex import complex

"""
A few simple tests for all methods in complex API.
Each test method returns nothing if passed and assertion error if failed.
"""

z, w = complex(2, 3), complex(-1, 8)

def test_add():
    assert z + w == complex(1, 11)

def test_sub():
    assert z - w == complex(3, -5)

def test_conjugate():
    assert z.conjugate() == complex(2, -3)

def test_modulus():
    eps = 1e-16
    assert sqrt(2**2 + 3**2) - eps <= z.modulus() <= sqrt(2**2 + 3**2) + eps

def test_eq():
    if z == w:
        print("Test failed")

#3.4
def test_radd():
    assert (2+2j) + complex(2, 3) == complex(4, 5)

def test_rsub():
    assert (2+2j) - complex(1, 3) == complex(1, -1)

def test_rmul():
    assert 4*complex(3, 4) - 2 == complex(10, 16)

if __name__ == '__main__':
    test_add(), test_sub(), test_conjugate(), test_modulus(), test_eq()
    test_radd(), test_rsub(), test_rmul()
