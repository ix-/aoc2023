def apply_func_line_by_line(filename: str, func):
    for line in open(filename):
        yield func(line)

def translate_words_to_numbers(line: str) -> int:
    """parse the line and translate numbers from 1 - 9 (e.g. 'two' -> 2)
    """
    lookup = {"one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9,
             }
    for key in lookup:
        if (pos := line.find(key)) != -1:
            prefix, suffix = line[:pos], line[pos+len(key):]
            line = "".join([prefix, key[0], str(lookup[key]), key[-1], suffix])
    return line
