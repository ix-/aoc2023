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
    output = translate_words_to_numbers(test_line)
    assert all([
        "1" in output,
        "2" in output,
        "3" in output,
        "4" in output,
        "5" in output,
        "6" in output,
        "7" in output,
        "8" in output,
        "9" in output,
    ])
