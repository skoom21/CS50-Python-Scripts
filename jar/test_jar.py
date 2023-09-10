from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(10)
    assert jar.capacity == 10
    try:
        jar = Jar(-1)
    except ValueError:
        assert True
    else:
        assert False
    
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert jar.size == 12
    assert str(jar) == "🍪"*12
    try:
        jar.deposit(1)
    except ValueError:
        assert True
    else:
        assert False
    ...


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar.size == 11
    assert str(jar) == "🍪"*11
    try:
        jar.withdraw(12)
    except ValueError:
        assert True
    else:
        assert False
    ...