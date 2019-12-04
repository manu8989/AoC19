#!/usr/bin/env python


import os
import sys
import math


def test_two_adjacent_numbers_exist_example1():
    assert single_two_adjacent_numbers_exist(112233) == True

def test_two_adjacent_numbers_exist_example2():
    assert single_two_adjacent_numbers_exist(123444) == False

def test_two_adjacent_numbers_exist_example3():
    assert single_two_adjacent_numbers_exist(111122) == True

def test_do_numbers_increase_example1():
    assert do_numbers_increase(123789) == True

def test_do_numbers_increase_example2():
    assert do_numbers_increase(111111) == True

def test_do_numbers_increase_example3():
    assert do_numbers_increase(135529) == False


def single_two_adjacent_numbers_exist(number):
    same_cnt = 1
    adjacent_numbers = []
    last_number = str(number)[0]
    for i in range(1,len(str(number))):
        if last_number == str(number)[i]:
            same_cnt += 1
            if i == len(str(number))-1:
                adjacent_numbers.append(same_cnt)
        else:
            adjacent_numbers.append(same_cnt)
            same_cnt = 1
        last_number = str(number)[i]
    return any([2 in adjacent_numbers])


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
        if single_two_adjacent_numbers_exist(number) and do_numbers_increase(number):
            cnt += 1
    print(cnt)
