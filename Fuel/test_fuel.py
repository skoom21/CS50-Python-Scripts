from fuel import convert, gauge
import pytest

def test_valid_fraction():
    assert convert("2/4") == 50

def test_invalid_fraction():
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_non_integer_values():
    with pytest.raises(ValueError):
        convert("2.5/4")
    with pytest.raises(ValueError):
        convert("2/4.5")

def test_less_than_1():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_greater_than_99():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_other_values():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
