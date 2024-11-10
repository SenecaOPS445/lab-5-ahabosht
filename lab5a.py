#!/usr/bin/env python3
# Student ID: 127098218
# Seneca Username: ahabosht

def read_file_string(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    f = open(file_name, 'r')
    data = [line.strip() for line in f]
    f.close()
    return data

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
