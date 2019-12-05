#!/usr/bin/env python


import os
import sys
import math


def test_exectue_program_example1():
    assert execute_program([1,0,0,0,99]) == [2,0,0,0,99]

def test_exectue_program_example2():
    assert execute_program([2,3,0,3,99]) == [2,3,0,6,99]

def test_exectue_program_example3():
    assert execute_program([2,4,4,5,99,0]) == [2,4,4,5,99,9801]

def test_exectue_program_example4():
    assert execute_program([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]


def read_program(filepath):
    program = []
    with open(filepath) as file:
        filecontent = file.read()
        tmp = filecontent.split(',')
        for t in tmp:
            program.append(int(t))
    return program

def execute_program(program):
    step = 0
    while step < len(program) and program[step] != 99:
        program, step = exectue_program_step(step, program)
    return program

def exectue_program_step(step, program):
    
    input1_index = program[step+1]
    input2_index = 0
    input3_index = 0

    if program[step] == 1 or program[step] == 2:
        input2_index = program[step+2]
        input3_index = program[step+3]

    if program[step] == 1:
        program[input3_index] = program[input1_index] + program[input2_index]
        step += 4
    elif program[step] == 2:
        program[input3_index] = program[input1_index] * program[input2_index]
        step += 4
    elif program[step] == 3:
        program[input1_index] = int(input("Input: "))
        step += 2
    elif program[step] == 4:
        print("Output: " + str(program[input1_index]))
        step += 2
    else:
        print("invalid input " + str(program[step]))
    
    return (program, step)


if __name__ == "__main__":
    program = read_program("input.txt")
    program = execute_program(program)
