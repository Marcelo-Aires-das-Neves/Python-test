import pytest
from convert import convert

def test_int_convert():
    assert convert(1) == 149597870700
    assert convert(2) == 299195741400
    assert convert(3) == 448793612100


def test_error():
    with pytest.raises(TypeError):
        convert("1")

        
def test_float_convert():
    assert convert(0.001) == pytest.approx(149597870.691) #149597870.691
    assert convert(0.002) == pytest.approx(299195741.382) #299195741.382
   