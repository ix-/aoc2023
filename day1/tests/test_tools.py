from ..tools import apply_func_line_by_line

def test_apply_func_line_by_line_reads_faithfully():
    tf = apply_func_line_by_line("tests/test_file.txt", lambda x: x)
    assert next(tf) == "1abc2\n" 
    assert next(tf) == "pqr3stu8vwx\n" 
    assert next(tf) == "a1b2c3d4e5f\n" 
    assert next(tf) == "treb7uchet\n" 

def test_apply_func_line_by_line_hits_every_line():
    tf = apply_func_line_by_line("tests/test_file.txt", lambda x: None)
    assert len([_ for _ in tf]) == 4
