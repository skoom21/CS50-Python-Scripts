from um import count

def test_valid_format_1():
    assert count("um?") == 1

def test_valid_format_2():
    assert count("Um, thanks for the album.") == 1

def test_valid_format_uppercase():
    assert count("um") == 1

def test_valid_format_mixed_case():
    assert count("Um, thanks, um...") == 2


