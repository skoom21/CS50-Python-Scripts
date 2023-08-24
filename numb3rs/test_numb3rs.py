from numb3rs import validate


def test_ip ():
    assert validate("127.0.0.1")
    assert validate("1.2.3.4")
    assert validate("255.255.255.0")
    assert not validate("275,3,6,28")
    assert not validate("512.512.512.512")
    assert not validate("1.2.3.1000")
    assert not validate("cat")
    assert not validate("10.256.256.256") 
    