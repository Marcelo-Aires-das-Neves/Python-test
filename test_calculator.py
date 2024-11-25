from calculator import squared
    
def test_square():
    assert squared(2) == 4
    assert squared(3) == 9
    assert squared(-2) == 4
    assert squared(-3) == 9
    assert squared(0) == 0
    
    

