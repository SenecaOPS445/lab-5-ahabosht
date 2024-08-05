#!/usr/bin/env python3
#Student ID: 127098218

def read_file_string(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(f"{line}\n")

def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as file_in, open(file_name_write, 'w') as file_out:
        for idx, line in enumerate(file_in, 1):
            file_out.write(f"{idx}:{line}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    open(file1, 'w').close()
    open(file2, 'w').close()
    open(file3, 'w').close()

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
