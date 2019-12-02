#!/usr/bin/env python

import os
import sys
import math

import numpy as np
import matplotlib.pyplot as plt


def calc_fuel(mass):
    return max(int(mass / 3) - 2, 0)

def test_calc_fuel_example1():
    assert calc_fuel(12) == 2

def test_calc_fuel_example2():
    assert calc_fuel(14) == 2

def test_calc_fuel_example3():
    assert calc_fuel(1969) == 654

def test_calc_fuel_example4():
    assert calc_fuel(100756) == 33583

if __name__ == "__main__":
    filepath = 'input.txt'
    sum = 0
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            sum += calc_fuel(int(line.strip()))
    print(sum)
