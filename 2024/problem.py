import os
import sys

def inp(filepath):
    with open(filepath) as file:
        line = file.read()
        data = ...
    return data

def part1(filepath):
    pass

def part2(filepath):
    pass

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == '1':
        print(f'Part 1: {part1(sys.argv[1])}')
    elif len(sys.argv) > 2 and sys.argv[2] == '2':
        print(f'Part 2: {part2(sys.argv[1])}')
    else:
        print(f'Part 1: {part1(sys.argv[1])}')
        print(f'Part 2: {part2(sys.argv[1])}')
