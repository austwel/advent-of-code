import sys
from pathlib import Path
from numpy import transpose
from collections import Counter
from aocd import data

data = [sorted(a) for a in transpose([[int(i) for i in line.strip().split('   ')] for line in data.split('\n')])]

def part1():
    return sum([abs(data[0][i]-data[1][i]) for i in range(len(data[0]))])

def part2():
    return sum([Counter(data[1]).get(n, 0)*n for n in data[0]])

if __name__ == "__main__":
    print(f' -- Advent of Code: Day {Path(__file__).stem} --')
    if len(sys.argv) < 2 or sys.argv[1] == '1':
        print(f' -> Part 1: {part1()}')
    if len(sys.argv) < 2 or sys.argv[1] == '2':
        print(f' -> Part 2: {part2()}')
