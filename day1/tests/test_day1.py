from ..day1 import get_coordinates, day1


#def test_get_coordinates_returns_a_two_digit_number():
#    assert 9 < len(get_coordinates( < 100

def test_1abc2():
    assert get_coordinates("1abc2") == 12

def test_pqr3stu8vwx():
    assert get_coordinates("pqr3stu8vwx") == 38

def test_a1b2c3d4e5f():
    assert get_coordinates("a1b2c3d4e5f") == 15

def test_treb7uchet():
    assert get_coordinates("treb7uchet") == 77

def test_two1nine():
    assert get_coordinates("two1nine") == 29

def test_eightwothree():
    assert get_coordinates("eightwothree") == 83

def test_abcone2threexyz():
    assert get_coordinates("abcone2threexyz") == 13

def test_xtwone3four():
    assert get_coordinates("xtwone3four") == 24

def test_4nineeightseven2():
    assert get_coordinates("4nineeightseven2") == 42

def test_zoneight234():
    assert get_coordinates("zoneight234") == 14

def test_7pqrstsixteen():
    assert get_coordinates("7pqrstsixteen") == 76

def test_eighthree():
    assert get_coordinates("eighthree") == 83

def test_4twoknkb39two():
    assert get_coordinates("4twoknkb39two") == 42

def test_five():
    assert get_coordinates("five") == 55

def test_threefivethree():
    assert get_coordinates("threefivethree") == 33

def test_fiveeight3sppjtccnineeighteightnffgtlsdj():
    assert get_coordinates("fiveeight3sppjtccnineeighteightnffgtlsdj") == 58

def test_threethreetwothree():
    assert get_coordinates("threethreetwothree") == 33

def test_five4five4():
    assert get_coordinates("five4five4") == 54

def test_day1():
    assert day1("tests/test_file.txt") == 281
