import sys
from math import prod

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    print([1, 2, 3, 4, 5][::5-1])
    return puzzle_input.split('\n')

def part1(data: list[str]) -> int:
    return sum(int("".join(c for c in l if c.isnumeric())) for l in data)

#def part2(data: list[str]) -> int:
#    return sum(int([c for c in l if c.isnumeric()][0]+[c for c in l if c.isnumeric()][-1]) for l in data)

names = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

def can_it_make_a_number(string: str, index: int) -> int:
    for name in names:
        if name == string[index:index+len(name)]:
            return names.index(name)+1
    return 0
    
#Solve Part 2
def part2(data) -> int:
    total = 0
    for line in data:
        line: str
        a = b = None
           
        line:str 
        for idx in range(len(line)):
            nummy = can_it_make_a_number(line, idx)
            if nummy != 0:
                if a is None:
                    a = str(nummy)
                b = str(nummy)
            elif line[idx].isnumeric():
                if a is None:
                    a = line[idx]
                b = line[idx]
        value = int(f'{a}{b}')
        total = total + value
    return total

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    f = open('test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'input.txt', 'r')
    puzzle_input = f.read().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))