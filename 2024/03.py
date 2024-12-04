import sys
from pathlib import Path
import re
from functools import reduce
from operator import mul
from aocd import data

def part1():
    return sum([reduce(mul, [int(i) for i in match.split(',')]) for match in re.findall(r'mul\((\d+,\d+)\)', data)])

def part2():
    on = True
    sum = 0
    for match in re.findall(r"mul\((\d+,\d+)\)|(do)\(\)|(don't)\(\)", data):
        if match[1]: on = True
        elif match[2]: on = False
        elif on: sum += reduce(mul, [int(i) for i in match[0].split(',')])
    return sum

if __name__ == "__main__":
    print(f' -- Advent of Code: Day {Path(__file__).stem} --')
    if len(sys.argv) < 2 or sys.argv[1] == '1':
        print(f' -> Part 1: {part1()}')
    if len(sys.argv) < 2 or sys.argv[1] == '2':
        print(f' -> Part 2: {part2()}')
