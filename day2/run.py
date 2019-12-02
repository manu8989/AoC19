#!/usr/bin/env python


import os
import sys
import math


def test_exectue_program_step_example1():
    assert execute_program([1,0,0,0,99]) == [2,0,0,0,99]

def test_exectue_program_step_example2():
    assert execute_program([2,3,0,3,99]) == [2,3,0,6,99]

def test_exectue_program_step_example3():
    assert execute_program([2,4,4,5,99,0]) == [2,4,4,5,99,9801]

def test_exectue_program_step_example4():
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
        program = exectue_program_step(step, program)
        step += 4
    return program

def exectue_program_step(step, program):
    
    if program[step] == 1:
        res = program[program[step+1]] + program[program[step+2]]
        program[program[step+3]] = res
    elif program[step] == 2:
        res = program[program[step+1]] * program[program[step+2]]
        program[program[step+3]] = res
    else:
        print("invalid input " + str(program[step]))
    return program


if __name__ == "__main__":
    
    program = read_program("input.txt")

    program[1] = 12
    program[2] = 2

    program = execute_program(program)

    print(program)
