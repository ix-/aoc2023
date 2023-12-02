def apply_func_line_by_line(filename, func):
    for line in open(filename):
        yield func(line)
