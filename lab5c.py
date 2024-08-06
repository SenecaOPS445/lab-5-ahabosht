#!/usr/bin/env python3
#Student ID: 127098218

def add(number1, number2):
    try:
        result = float(number1) + float(number2)
        return result
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (IOError, FileNotFoundError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))
    print(add('10', 5))
    print(add('abc', 5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
