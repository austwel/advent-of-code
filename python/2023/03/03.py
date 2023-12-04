import sys
from itertools import product

#Parse Puzzle input
def parse(puzzle_input: str) -> list[str]:
    return puzzle_input.split('\n')

#Solve Part 1
def part1(lines: list[str]) -> int:
    total = 0
    for r in range(len(lines)):
        c = 0
        while c < len(lines[r]):
            if lines[r][c].isnumeric():
                n = generate_number(lines[r], c)
                if is_part(lines, r, c, len(str(n))): 
                    total += n
                c += len(str(n))-1
            c+=1
    return total

def is_part(lines: list[str], r: int, c: int, l: int) -> bool:
    for idx, rowdelta, coldelta in list(product(list(range(c, c+l)),[-1,0,1],[-1,0,1])):
        if 0<=r+rowdelta<len(lines) and 0<=idx+coldelta<len(lines[r]) and lines[r+rowdelta][idx+coldelta] != '.': return True

def generate_number(line: str, startIdx: int) -> int:
    if startIdx>=len(line) or not line[startIdx].isnumeric(): return ''
    return int(f'{line[startIdx]}{generate_number(line, startIdx+1)}')
    
#Solve Part 2
def part2(lines) -> int:
    total = 0
    gears: dict[tuple[int,int], list[int]] = {}
    for r in range(len(lines)):
        c = 0
        while c < len(lines[r]):
            if lines[r][c].isnumeric():
                n = generate_number(lines[r], c)
                n_len = len(str(n))
                attached_gears = is_part2(lines, r, c, n_len)
                for gr, gc in attached_gears:
                    if (gr,gc) in gears.keys():
                        gears[(gr,gc)].append(n)
                    else:
                        gears[(gr,gc)] = [n]
                c += n_len-1
            c+=1
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]
    return total

def is_part2(lines: list[str], r, c, l) -> list[tuple[str, int, int]]:
    #Check left
    attached_gears = []
    if c != 0:
        if lines[r][c-1] == '*': 
            attached_gears.append((r, c-1))
    #Check right
    if c+l != len(lines[r]):
        if lines[r][c+l] == '*': attached_gears.append((r, c+l))
    #Check under
    if r != len(lines)-1:
        for i in range(l+2):
            if c+i-1 < 0 or c+i >= len(lines[r]): continue
            if lines[r+1][c+i-1] == '*': attached_gears.append((r+1, c+i-1))
    #Check over
    if r != 0:
        for i in range(l+2):
            if c+i-1 < 0 or c+i >= len(lines[r]): continue
            if lines[r-1][c+i-1] == '*': attached_gears.append((r-1, c+i-1))
    return attached_gears

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    data = parse(puzzle_input)
    solution1 = part1(data)
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