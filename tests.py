"""
Tests for the calc module
"""
import calc

def test_sum():
    assert(calc.sum(2,3) == 5)
    
def test_sub():
    assert(calc.sub(5, 1) == 4)
    
def test_div():
    assert(calc.div(8, 2) == 4)
    
def test_exp():
    assert(calc.exp(2,3) == 8)

def test_factorize():
    assert(calc.factorize(6) == [2, 3])
    assert(calc.factorize(8) == [2, 2, 2])

