from ..tools import apply_func_line_by_line
from ..tools import translate_words_to_numbers

def test_apply_func_line_by_line_reads_faithfully():
    tf = apply_func_line_by_line("tests/test_file.txt", lambda x: x)
    assert next(tf) == "two1nine\n" 

def test_apply_func_line_by_line_hits_every_line():
    tf = apply_func_line_by_line("tests/test_file.txt", lambda x: None)
    assert len([_ for _ in tf]) == 7

def test_translate_words_to_numbers_finds_1_to_9():
    test_line = "nineeightsevensixfivefourthreetwoone"
    assert translate_words_to_numbers(test_line) == '987654321'

def test_translate_words_to_numbers_doesnt_find_zero():
    assert translate_words_to_numbers("badzerodeadbeef") == "badzerodeadbeef"
