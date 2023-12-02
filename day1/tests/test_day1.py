from ..day1 import get_coordinates, day1

def helper(input_string, output_string):
    return get_coordinates(input_string) == output_string

#def test_get_coordinates_returns_a_two_digit_number():
#    assert 9 < len(get_coordinates()) < 100

def test_1abc2():
    assert helper("1abc2", 12)

def test_pqr3stu8vwx():
    assert helper("pqr3stu8vwx", 38)

def test_a1b2c3d4e5f():
    assert helper("a1b2c3d4e5f", 15)

def test_treb7uchet():
    assert helper("treb7uchet", 77)

def test_day1():
    assert day1("tests/test_file.txt") == 142
