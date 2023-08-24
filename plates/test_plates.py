from plates import is_valid


def test_aplhabeticalchecks():
    # alphabets and numbers
    assert not is_valid('A123')
    assert not is_valid('123ABC')

def test_Alphanumeric():
    assert not is_valid('PI3.14')

    
    
def test_zeroPlacement():
    assert not is_valid('CS05')
    assert not is_valid('CS50P2')
    
def test_length():
    assert not is_valid('H')
    
    
    