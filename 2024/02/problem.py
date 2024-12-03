import os
import sys
import numpy

def inp(filepath):
    with open(filepath) as file:
        lines = file.read().strip().split('\n')
        return [[int(i) for i in l.split(' ')] for l in lines]

def part1(filepath):
    return len([True for report in inp(filepath) if not any([True for diff in [report[i]-report[i+1] for i in range(len(report)-1)] if diff < -3 or diff >= 0]) or not any ([True for diff in [report[i]-report[i+1] for i in range(len(report)-1)] if diff > 3 or diff <= 0])])

def part2(filepath):
    count = 0
    data = inp(filepath)
    for report in data:
        diffs = [report[i]-report[i+1] for i in range(len(report)-1)]
        if not any([True for diff in diffs if diff < -3 or diff >= 0]):
            count +=1
            continue
        if not any([True for diff in diffs if diff > 3 or diff <= 0]):
            count +=1
            continue
        for i in range(len(report)):
            r2 = list(numpy.delete(report, i))
            d2 = [r2[i]-r2[i+1] for i in range(len(r2)-1)]
            if not any([True for diff in d2 if diff < -3 or diff >= 0]):
                count +=1
                break
            if not any([True for diff in d2 if diff > 3 or diff <= 0]):
                count +=1
                break
    return count

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == '1':
        print(f'Part 1: {part1(sys.argv[1])}')
    elif len(sys.argv) > 2 and sys.argv[2] == '2':
        print(f'Part 2: {part2(sys.argv[1])}')
    else:
        print(f'Part 1: {part1(sys.argv[1])}')
        print(f'Part 2: {part2(sys.argv[1])}')
