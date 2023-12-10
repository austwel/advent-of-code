import sys

import math
#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    instructions = puzzle_input.split('\n')[0]
    lr = {line.split('=')[0].strip(): (line.split('=')[1].split(',')[0].replace('(', '').strip(),line.split('=')[1].split(',')[1].replace(')', '').strip()) for line in puzzle_input.split('\n')[2:]}
    return instructions, lr

#Solve Part 1
def part1(instructions: str, lr: dict[str, tuple[str, str]]) -> int:
    instruction_count = 0
    location = 'AAA'
    while True:
        curr_ins = instructions[instruction_count % len(instructions)]
        location = lr[location][0] if curr_ins == 'L' else lr[location][1]
        instruction_count+=1
        if location == 'ZZZ': return instruction_count

from math import gcd
#Solve Part 2
def part2(instructions: str, lr: dict[str, tuple[str, str]]) -> int:
    starting_nodes = [node for node in lr.keys() if node[-1] == 'A']
    distances = []
    for node in starting_nodes:
        instruction_count = 0
        location = node
        while True:
            curr_ins = instructions[instruction_count % len(instructions)]
            location = lr[location][0] if curr_ins == 'L' else lr[location][1]
            instruction_count+=1
            if location[-1] == 'Z': 
                distances.append(instruction_count)
                break
    lcm = 1
    for i in distances:
        lcm = lcm*i//gcd(lcm,i)
    return lcm

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    instructions, lr = parse(puzzle_input)
    solution1 = 1 #solution1 = part1(instructions, lr)
    solution2 = part2(instructions, lr)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    f = open('test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'input.txt', 'r')
    puzzle_input = f.read().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))