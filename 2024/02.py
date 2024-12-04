import sys
from pathlib import Path
import numpy
from aocd import data

data = [[int(i) for i in l.split(' ')] for l in data.strip().split('\n')]

def part1():
    return len([True for report in data if not any([True for diff in [report[i]-report[i+1] for i in range(len(report)-1)] if diff < -3 or diff >= 0]) or not any ([True for diff in [report[i]-report[i+1] for i in range(len(report)-1)] if diff > 3 or diff <= 0])])

def part2():
    count = 0
    for report in data:
        ds = [report[i]-report[i+1] for i in range(len(report)-1)]
        if not any([1 for d in ds if d < -3 or d >= 0]) or not any ([1 for d in ds if d > 3 or d <= 0]):
            count +=1
            continue
        for i in range(len(report)):
            r2 = list(numpy.delete(report, i))
            d2 = [r2[i]-r2[i+1] for i in range(len(r2)-1)]
            if not any([1 for d in d2 if d < -3 or d >= 0]) or not any([1 for d in d2 if d > 3 or d <= 0]):
                count +=1
                break
    return count

if __name__ == "__main__":
    print(f' -- Advent of Code: Day {Path(__file__).stem} --')
    if len(sys.argv) < 2 or sys.argv[1] == '1':
        print(f' -> Part 1: {part1()}')
    if len(sys.argv) < 2 or sys.argv[1] == '2':
        print(f' -> Part 2: {part2()}')
