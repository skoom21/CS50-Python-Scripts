from twttr import shorten

def test_lowercase():
    assert shorten("fadsfa") == "fdsf"
    
def test_uppercase():
    assert shorten("fAdsfa") == "fdsf"

def test_numbers():
    assert shorten("fAdsfa1") == "fdsf1"
    
def test_punctuations():
    assert shorten("fAdsfa!") == "fdsf!"