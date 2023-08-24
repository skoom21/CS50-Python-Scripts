import pytest
from working import convert

def test_valid_format_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_format_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_format_uppercase():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_valid_format_mixed_case():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

