import pytest

from mypkg.poww import poww 

def test_1():
	assert(poww(2,5) == 32)

def test_2():
	assert(pow(2,4) == 16)
	
def test_3():
	assert(pow(3, 3) == 27)
