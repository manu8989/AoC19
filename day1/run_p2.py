#!/usr/bin/env python


import os
import sys
import math


def test_calc_fuel_example1():
    assert calc_fuel(12) == 2

def test_calc_fuel_example2():
    assert calc_fuel(14) == 2

def test_calc_fuel_example3():
    assert calc_fuel(1969) == 966

def test_calc_fuel_example4():
    assert calc_fuel(100756) == 50346


def calc_fuel(mass):
    fuel = max(int(mass / 3) - 2, 0)
    if fuel > 0:
        return fuel + calc_fuel(fuel)
    else:
        return 0


if __name__ == "__main__":
    filepath = 'input.txt'
    sum = 0
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            sum += calc_fuel(int(line.strip()))
    print(sum)
