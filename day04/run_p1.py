#!/usr/bin/env python


import os
import sys
import math


def test_two_adjacent_numbers_exist_example1():
    assert two_adjacent_numbers_exist(123789) == False

def test_two_adjacent_numbers_exist_example2():
    assert two_adjacent_numbers_exist(111111) == True

def test_two_adjacent_numbers_exist_example3():
    assert two_adjacent_numbers_exist(135529) == True

def test_do_numbers_increase_example1():
    assert do_numbers_increase(123789) == True

def test_do_numbers_increase_example2():
    assert do_numbers_increase(111111) == True

def test_do_numbers_increase_example3():
    assert do_numbers_increase(135529) == False


def two_adjacent_numbers_exist(number):
    return any([digits in str(number) for digits in ["00","11","22","33","44","55","66","77","88","99"]])

def do_numbers_increase(number):
    for i in range(len(str(number))-1):
        if(int(str(number)[i]) > int(str(number)[i+1])):
            return False
    return True


if __name__ == "__main__":
    lower_boundary = 372037
    upper_boundary = 905157
    cnt = 0
    for number in range(lower_boundary, upper_boundary+1):
        if two_adjacent_numbers_exist(number) and do_numbers_increase(number):
            cnt += 1
    print(cnt)
