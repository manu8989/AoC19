#!/usr/bin/env python


import os
import sys
import math


def test_create_path_example1():
    assert create_path("R8,U5,L5,D3") == [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2)]

def test_create_path_example2():
    assert create_path("U7,R6,D4,L4") == [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3)]

def test_find_crossings():
    assert [(0, 0), (3, 3), (6, 5)] == find_crossings([[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2)],[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3)]])

def test_calc_distance_example1():
    assert calc_distance((3,4)) == 7

def test_calc_distance_example2():
    assert calc_distance((-3,4)) == 7

def test_calc_distance_example3():
    assert calc_distance((3,-4)) == 7

def test_calc_distance_example4():
    assert calc_distance((-3,-4)) == 7

def test_chain_example1():
    assert find_shortest_distance(find_crossings([create_path("R75,D30,R83,U83,L12,D49,R71,U7,L72"),create_path("U62,R66,U55,R34,D71,R55,D58,R83")])) == 159

def test_chain_example2():
    assert find_shortest_distance(find_crossings([create_path("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"),create_path("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")])) == 135


def read_wires(filepath):
    wirepaths = []
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            wirepaths.append(create_path(line.strip()))
    return wirepaths

def create_path(steps):
    path = []
    steplist = steps.split(',')
    pos_x = 0
    pos_y = 0
    for step in steplist:
        if step[0] == 'R':
            for i in range(int(step[1:])):
                pos_x += 1
                path.append((pos_x, pos_y))
        elif step[0] == 'D':
            for i in range(int(step[1:])):
                pos_y -= 1
                path.append((pos_x, pos_y))
        elif step[0] == 'L':
            for i in range(int(step[1:])):
                pos_x -= 1
                path.append((pos_x, pos_y))
        elif step[0] == 'U':
            for i in range(int(step[1:])):
                pos_y += 1
                path.append((pos_x, pos_y))
    return path

def find_crossings(wires):
    common = list(set(wires[0]).intersection(wires[1]))
    for i in range(2,len(wires)):
        common = list(set(common).intersection(wires[i]))
    return common

def calc_distance(point):
    return abs(point[0]) + abs(point[1])

def find_shortest_distance(crossings):
    return min([calc_distance(point) for point in crossings])


if __name__ == "__main__":
    wirepaths = read_wires("input.txt")
    crossings = find_crossings(wirepaths)
    nearest_crossing = find_shortest_distance(crossings)
    print(nearest_crossing)
