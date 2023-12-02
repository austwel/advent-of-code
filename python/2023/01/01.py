import sys

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

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    return puzzle_input.split('\n')

#Solve Part 1
def part1(data: list[str]) -> int:
    total = 0
    for line in data:
        a = b = None
        for char in line:
            if char.isnumeric():
                if a is None:
                    a = char
                b = char
        value = int(f'{a}{b}')
        print(a, b, value)
        total = total + value
    return total

def can_it_make_a_number(string: str, index: int) -> int:
    print(string, index)
    for name in names:
        if name == string[index:index+len(name)]:
            print(names.index(name)+1)
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
        print(a, b, value)
        total = total + value
    return total

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    data = parse(puzzle_input)
    solution1 = 1#part1(data)
    solution2 = part2(data)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        f = open('test.txt', 'r')
        puzzle_input = f.read().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
    else:
        f = open('input.txt', 'r')
        puzzle_input = f.read().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))