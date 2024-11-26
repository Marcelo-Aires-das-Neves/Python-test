from hello2 import hello2


def test_default():
    assert hello2() == "Hello, World"
    
def test_argument():
    assert hello2("David") == "Hello, David"
    


