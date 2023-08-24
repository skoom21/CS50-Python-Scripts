from bank import value

def test_value():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("hi") == 20
    assert value("oh hello!") == 100

def test_incorrectValue():
    assert value("hello") != 100
    assert value("h") != 100
    assert value("hi") != 100
    assert value("oh hello!") != 0
    
def test_caseInsensivity():
    assert value("hello") == value("HELLO")
    assert value("h") == value("H")
    assert value("hi") == value("HI")
    assert value("oh hello!") == value("OH HELLO!")