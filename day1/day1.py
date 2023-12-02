#! /bin/env python3

from tools import apply_func_line_by_line, translate_words_to_numbers

def digit_parser(line: str) -> str:
    return [char for char in line if char.isdigit()]

def line_parser(line: str) -> str:
    line = translate_words_to_numbers(line)
    line = digit_parser(line)
    return line

def get_coordinates(line: str) -> int:
    return int(line_parser(line)[0]+line_parser(line)[-1])

def day1(filename: str) -> int:
    sum(
        [line for line in apply_func_line_by_line(filename, get_coordinates)]
    )

if __name__ == "__main__":
    print(f"Day 1: {day1_1('day1.txt')}")
