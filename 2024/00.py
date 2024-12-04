import sys
from pathlib import Path
from aocd import data

def part1():
    pass

def part2():
    pass

if __name__ == "__main__":
    print(f' -- Advent of Code: Day {Path(__file__).stem} --')
    if len(sys.argv) < 2 or sys.argv[1] == '1':
        print(f' -> Part 1: {part1()}')
    if len(sys.argv) < 2 or sys.argv[1] == '2':
        print(f' -> Part 2: {part2()}')
