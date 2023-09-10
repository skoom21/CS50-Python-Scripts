import pytest
from seasons import validDate

#Multiple functions to text validDate
def test_validDate():
    assert validDate("2022-09-02") == "Five hundred twenty-five thousand, six hundred minutes"

def test_validDate1():
    assert validDate("2021-09-02") == "One million, fifty-one thousand, two hundred minutes"
    
    
def test_invalidDate():
    with pytest.raises(SystemExit):
        validDate("January-1-15")
    
# def test_invalidDate3():
#     assert validDate("2000-01-32") == "Invalid Date"
